# Django Core
from django.db import models
# Owner
from accounts.models import User
from courses.models import Course
from reusable.models import TimeStampModel
from reusable.constants import REQUIRED, BLANK
from .choices import TYPE_QUESTION


class Lesson(TimeStampModel):
    title = models.CharField(max_length=120, **REQUIRED)
    score_approved = models.PositiveIntegerField(**REQUIRED)
    is_approved = models.BooleanField(default=False)
    previous_lesson = models.OneToOneField(
        'self',
        related_name='previous',
        verbose_name='Previous Lesson',
        on_delete=models.CASCADE,
        **BLANK
    )
    course = models.ForeignKey(
        Course,
        related_name='lessons',
        verbose_name='Course',
        on_delete=models.CASCADE,
        **REQUIRED
    )
    student = models.ManyToManyField(
        User,
        related_name='lessons',
        verbose_name='Student',
    )

    def __str__(self):
        return self.title.title()


class TypeQuestion(TimeStampModel):
    type_question = models.PositiveSmallIntegerField(default=1, choices=TYPE_QUESTION)

    def __str__(self):
        return self.get_type_question_display()


class Question(TimeStampModel):
    title = models.CharField(max_length=120, **REQUIRED)
    score = models.PositiveIntegerField()
    type_question = models.ForeignKey(
        TypeQuestion,
        related_name='questions',
        verbose_name='Type Question',
        on_delete=models.CASCADE,
        **REQUIRED
    )
    lesson = models.ForeignKey(
        Lesson,
        related_name='questions',
        verbose_name='Lesson',
        on_delete=models.CASCADE,
        **REQUIRED
    )

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return self.title.title()


class Answer(TimeStampModel):
    text = models.CharField(max_length=120, **REQUIRED)
    question = models.ForeignKey(
        Question,
        related_name='answers',
        verbose_name='Question',
        on_delete=models.CASCADE,
        **REQUIRED
    )

    class Meta:
        ordering = ('-pk', )

    def __str__(self):
        return self.text
