# Django
from django.shortcuts import get_object_or_404
# Thirdy Party Libraries
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
# Owner
from .serializers import LessonSerializer, QuestionListSerializer
from ...models import Lesson


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