# Django Core
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


    def __str__(self):
        return self.email

    def get_display_name(self):
        return f'{self.first_name} {self.last_name}'