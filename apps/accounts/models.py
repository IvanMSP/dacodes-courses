# Django Core
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
# Owner
from reusable.constants import REQUIRED


class User(AbstractUser):
    email = models.EmailField(unique=True, **REQUIRED)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


    def __str__(self):
        return self.email

    def set_user_type(self, user_type):
        if user_type == 'student':
            self.is_student = True
        else:
            self.is_teacher = True
        self.save()
    
    @property
    def user_type(self):
        if self.is_student:
            return 'student'
        else:
            return 'teacher'