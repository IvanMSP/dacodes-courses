# Django
from django.urls import path
# Dacodes Imports
from .views import CoursesView

courses_v1_urls = [
    path('v1/courses', CoursesView.as_view(), name='courses'),
]