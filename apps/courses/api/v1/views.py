# Django

# Thirdy Party Libraries
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework import filters
# Owner
from .serializers import CourseListSerializer
from ...models import Course


class CoursesView(ListAPIView):
    queryset = Course.objects.get_queryset().order_by('-created')
    serializer_class = CourseListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'teacher__first_name']