# Django
from django.urls import path
# Dacodes Imports
from .views import UserAuthToken


account_v1_urls = [
    path('v1/auth-token/', UserAuthToken.as_view(), name='auth-token'),
]