# Thirdy Party Libraries
from rest_framework import serializers

# Owner
from ...models import Course, Enrollment
from accounts.api.v1.serializers import TeacherSerializer
from lessons.api.v1.serializers import LessonListSerializer


class CourseSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()
    isApproved = serializers.BooleanField(source='is_approved')
    lessons = serializers.HyperlinkedIdentityField(
        read_only=True,
        lookup_field='slug',
        view_name='courses-lessons', 
    )

    class Meta:
        model = Course
        fields = (
            'id',
            'isApproved',
            'name',
            'slug',
            'created',
            'teacher',
            'lessons'
        )


class CourseListSerializer(serializers.ModelSerializer):
    previousCourse = CourseSerializer(source='previous_course')
    teacher = TeacherSerializer()

    class Meta:
        model = Course
        fields = (
            'id',
            'name',
            'slug',
            'created',
            'previousCourse',
            'teacher',
        )


class EnrollmentSerializer(serializers.ModelSerializer):
    student = serializers.HiddenField(default=serializers.CurrentUserDefault())
    course = CourseSerializer()
    
    class Meta:
        model = Enrollment
        fields = (
            'student',
            'course',
        )