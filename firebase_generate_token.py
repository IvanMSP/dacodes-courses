# Python's Libraries
import os

# Django's Libraries
from django.conf import settings
from decouple import config 

# Third-party Libraries
import firebase_admin
from firebase_admin import credentials, auth


file_cred = config('FIREBASE_KEY')
cred = credentials.Certificate(file_cred)

default_app = firebase_admin.initialize_app(cred)

uid = config('UID_USER_FIREBASE')

custom_token = auth.create_custom_token(uid)
print(custom_token)
