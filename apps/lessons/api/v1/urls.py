# Django
from django.urls import path
# Dacodes Imports
from .views import (
    LessonsDetailView,
    QuestionsListView
)


lessons_v1_urls = [
    path('v1/lessons/<int:pk>', LessonsDetailView.as_view(), name='lessons_detail'),
    path('v1/lessons/<int:pk>/questions', QuestionsListView.as_view(), name='lessons-questions'),
]