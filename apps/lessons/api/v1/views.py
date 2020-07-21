# Django
from django.shortcuts import get_object_or_404
# Thirdy Party Libraries
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
# Owner
from .serializers import LessonSerializer, QuestionListSerializer
from courses.models import Course
from ...models import Lesson, Question, Answer
from dacodes_framework.response import EnvelopeResponse, EnvelopeErrorResponse


class LessonsDetailView(RetrieveAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]
    queryset = Lesson.objects.all()


class QuestionsListView(ListAPIView, UpdateAPIView):
    serializer_class = QuestionListSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        lesson = get_object_or_404(Lesson, pk=self.kwargs.get('pk'))
        return lesson.questions.all()


class TakeLessonView(APIView):
    def post(self, request, pk):
        json_data = request.data
        instance_lesson = get_object_or_404(Lesson, pk=pk)
        if instance_lesson.is_approved:
            return EnvelopeErrorResponse('LESSON IS TAKES', status=status.HTTP_400_BAD_REQUEST)
        course = get_object_or_404(Course, pk=instance_lesson.course.pk)
        last_lesson = Lesson.objects.filter(course=course).last()
        points = []
        for item in json_data:
            instance_question = get_object_or_404(Question, pk=item.get('id'))
            for answer in item.get('answers'):
                instance_answer = get_object_or_404(Answer, pk=answer.get('id'))
                if answer.get('isCheck') and instance_answer.is_correct:
                    points.append(instance_question.score)
        if sum(points) >= instance_lesson.score_approved:
            instance_lesson.is_approved = True
            instance_lesson.save()
            if instance_lesson.pk == last_lesson.pk:
                course.is_approved = True
                course.save()
                return EnvelopeResponse('COURSE APPROVED', status=status.HTTP_200_OK)
            return EnvelopeResponse('LESSON APPROVED', status=status.HTTP_200_OK)    
        return EnvelopeErrorResponse('LESSON NOT APPROVED', status=status.HTTP_406_NOT_ACCEPTABLE)