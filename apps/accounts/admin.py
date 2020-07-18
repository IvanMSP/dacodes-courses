# Django Core
from django.contrib import admin

# Owner
from .models import User

admin.site.register(User)