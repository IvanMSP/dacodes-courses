# Django Core
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Owner
from .models import User


class UserAdmon(UserAdmin):
    pass

admin.site.register(User, UserAdmon)