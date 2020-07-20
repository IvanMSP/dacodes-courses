# Django Core
from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError

# Owner
from accounts.models import User
from reusable.models import TimeStampModel
from reusable.constants import REQUIRED, BLANK, BLANK_NOT_NULL


class Course(TimeStampModel):
    name = models.CharField(max_length=120, **REQUIRED)
    slug = models.SlugField(max_length=120, **BLANK_NOT_NULL)
    is_approved = models.BooleanField(default=False)
    previous_course = models.OneToOneField(
        'self',
        related_name='previous',
        verbose_name='previous course',
        on_delete=models.CASCADE,
        **BLANK
    )
    teacher = models.ForeignKey(
        User,
        related_name='courses',
        on_delete=models.CASCADE,
        verbose_name='Teacher',
        **REQUIRED
    )

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name.title()
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Course, self).save(*args, **kwargs)


class Enrollment(TimeStampModel):
    student = models.ForeignKey(
        User,
        related_name='courses_student',
        verbose_name='Student',
        on_delete=models.CASCADE,
        **REQUIRED
    )
    course = models.ForeignKey(
        Course,
        related_name='students',
        verbose_name='Course',
        on_delete=models.CASCADE,
        **REQUIRED
    )

    def __str__(self):
        return f'{self.course.name} - {self.student.get_full_name()}'

    def save(self, *args, **kwargs):
        if self.student.is_student:
            super(Enrollment, self).save(*args, **kwargs)
        else:
            raise ValidationError('User is not Student')