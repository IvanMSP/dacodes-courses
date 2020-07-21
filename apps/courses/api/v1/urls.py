# Django
from django.urls import path
# Dacodes Imports
from .views import (
    CoursesView, EnrollmentStudent, 
    CoursesDetailView, CoursesLessonsView
)


courses_v1_urls = [
    path('v1/courses', CoursesView.as_view(), name='courses'),
    path('v1/courses/<str:slug>', CoursesDetailView.as_view(), name='courses-detail'),
    path('v1/courses/<str:slug>/lessons', CoursesLessonsView.as_view(), name='courses-lessons'),
    path('v1/enrollments', EnrollmentStudent.as_view(), name='enrollment-student'),
]