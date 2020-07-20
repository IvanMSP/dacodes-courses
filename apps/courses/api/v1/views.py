# Django
from django.shortcuts import get_object_or_404
# Thirdy Party Libraries
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
# Owner
from .serializers import CourseListSerializer, EnrollmentSerializer, CourseSerializer
from lessons.api.v1.serializers import LessonListSerializer
from ...models import Course, Enrollment
from lessons.models import Lesson
from accounts.models import User


class CoursesView(ListAPIView):
    queryset = Course.objects.get_queryset().order_by('-created')
    serializer_class = CourseListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'teacher__first_name']


class CoursesDetailView(RetrieveAPIView):
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated]
    serializer_class =  CourseSerializer
    queryset = Course.objects.all()


class CoursesLessonsView(ListAPIView):
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated]
    serializer_class = LessonListSerializer
    
    def get_queryset(self):
        course = get_object_or_404(Course, slug=self.kwargs.get('slug'))
        return self.request.user.lessons.filter(course=course).order_by('-created')


class EnrollmentStudent(ListAPIView):
    lookup_field = 'username'
    permission_classes = [IsAuthenticated]
    serializer_class = EnrollmentSerializer
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Enrollment.objects.filter(student=user).order_by('-created')