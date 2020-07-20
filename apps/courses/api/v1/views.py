# Django
from django.shortcuts import get_object_or_404
# Thirdy Party Libraries
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
# Owner
from .serializers import CourseListSerializer, EnrollmentSerializer
from ...models import Course, Enrollment
from accounts.models import User


class CoursesView(ListAPIView):
    queryset = Course.objects.get_queryset().order_by('-created')
    serializer_class = CourseListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'teacher__first_name']


class EnrollmentStudent(ListAPIView):
    lookup_field = 'username'
    permission_classes = [IsAuthenticated]
    serializer_class = EnrollmentSerializer
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Enrollment.objects.filter(student=user).order_by('-created')