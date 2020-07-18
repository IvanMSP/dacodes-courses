# Django Core
from django.contrib import admin

# Owner
from .models import Course, Enrollment


admin.site.register(Course)
admin.site.register(Enrollment)