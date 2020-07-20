# Django
from django.urls import path
# Dacodes Imports
from .views import CoursesView, EnrollmentStudent

courses_v1_urls = [
    path('v1/courses', CoursesView.as_view(), name='courses'),
    path('v1/courses/<str:username>', EnrollmentStudent.as_view(), name='enrollment-student'),
]