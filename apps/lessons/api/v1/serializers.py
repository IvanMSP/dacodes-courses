# Thirdy Party Libraries
from rest_framework import serializers

# owner
from ...models import Lesson, Question, Answer, TypeQuestion


class TypeQuestionSerializer(serializers.ModelSerializer):
    typeQuestion = serializers.CharField(source='type_question')

    class Meta:
        model = TypeQuestion
        fields = (
            'id',
            'typeQuestion'
        )


class AnswerListSerializer(serializers.ModelSerializer):
    text = serializers.CharField(read_only=True)
    isCheck = serializers.BooleanField(source='is_check')

    class Meta:
        model = Answer
        fields = (
            'id',
            'text',
            'isCheck',
        )


class LessonSerializer(serializers.ModelSerializer):
    scoreApproved = serializers.IntegerField(source='score_approved')
    isApproved = serializers.BooleanField(source='is_approved')
    course = serializers.HyperlinkedRelatedField(
        read_only=True,
        lookup_field='slug',
        view_name='courses-detail', 
    )
    questions = serializers.HyperlinkedIdentityField(
        read_only=True,
        lookup_field='pk',
        view_name='lessons-questions',
    )

    class Meta:
        model = Lesson
        fields = (
            'id',
            'title',
            'created',
            'scoreApproved',
            'isApproved',
            'course',
            'questions'
        )


class LessonListSerializer(serializers.ModelSerializer):
    scoreApproved = serializers.IntegerField(source='score_approved')
    isApproved = serializers.BooleanField(source='is_approved')
    previousLesson = serializers.HyperlinkedRelatedField(
        read_only=True,
        lookup_field='pk',
        view_name='lessons_detail',
        source='previous_lesson' 
    )
    course = serializers.HyperlinkedRelatedField(
        read_only=True,
        lookup_field='slug',
        view_name='courses-detail', 
    )

    class Meta:
        model = Lesson
        fields = (
            'id',
            'title',
            'created',
            'scoreApproved',
            'isApproved',
            'previousLesson',
            'course'
        )


class QuestionListSerializer(serializers.ModelSerializer):
    typeQuestion = TypeQuestionSerializer(source='type_question', read_only=True)
    answers = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = (
            'id',
            'created',
            'title',
            'score',
            'typeQuestion',
            'lesson',
            'answers',
        )

    def get_answers(self, question):
        answers = question.answers.all()
        return AnswerListSerializer(answers, many=True).data