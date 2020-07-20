# Thirdy Party Libraries
from rest_framework import serializers

# Owner
from ...models import Course, Enrollment
from accounts.api.v1.serializers import TeacherSerializer


class CourseSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()
    scoreApproved = serializers.IntegerField(source='score_aproved')

    class Meta:
        model = Course
        fields = (
            'id',
            'name',
            'slug',
            'created',
            'teacher',
            'scoreApproved'
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


class EnrollmentSerializer(serializers.ModelSerializer):
    student = serializers.HiddenField(default=serializers.CurrentUserDefault())
    course = CourseSerializer()
    
    class Meta:
        model = Enrollment
        fields = (
            'student',
            'course',
        )