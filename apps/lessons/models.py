# Django Core
from django.db import models
# Owner
from reusable.models import TimeStampModel
from reusable.constants import REQUIRED, BLANK


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

    def __str__(self):
        return self.title.title()
