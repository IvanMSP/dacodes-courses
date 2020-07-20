# Thirdy Party Libraries
from rest_framework import serializers

# Owner
from ...models import Course
from accounts.api.v1.serializers import TeacherSerializer


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = (
            'id',
            'name',
            'slug',
            'created',
            'teacher',
        )


class CourseListSerializer(serializers.ModelSerializer):
    scoreApproved = serializers.IntegerField(source='score_aproved')
    previousCourse = CourseSerializer(source='previous_course')
    teacher = TeacherSerializer()

    class Meta:
        model = Course
        fields = (
            'id',
            'name',
            'slug',
            'created',
            'scoreApproved',
            'previousCourse',
            'teacher',
        )