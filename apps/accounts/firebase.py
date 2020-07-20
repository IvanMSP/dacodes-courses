
# -*- coding: utf-8 -*-

# Python's Libraries
import os

# Django's Libraries
from django.conf import settings

# Third-party Libraries
import firebase_admin
from firebase_admin import credentials, auth, messaging
from rest_framework.exceptions import NotAuthenticated


file_cred = os.path.abspath(
    os.path.join(
        os.getcwd(),
        settings.FIREBASE_KEY
    )
)

cred = credentials.Certificate(file_cred)

default_app = firebase_admin.initialize_app(cred)


class FireBaseAccountNotExist(Exception):
    pass


class FirebaseHelper(object):

    @staticmethod
    def get_token(token):
        """Metodo que verifica un token de Firebase."""
        try:
            decoded_token = auth.verify_id_token(token)
            return decoded_token

        except ValueError:
            raise NotAuthenticated(
                "Invalid Token"
            )

    @staticmethod
    def get_email(token):
        """Metodo que verifica un token de Firebase."""
        try:
            decoded_token = auth.verify_id_token(token)
            email = decoded_token['email']
            return email

        except ValueError:
            raise NotAuthenticated(
                "Invalid Token"
            )

    @staticmethod
    def get_number(token):
        """Metodo que verifica un token de Firebase."""
        try:
            decoded_token = auth.verify_id_token(token)
            number = decoded_token['phone_number']
            if '+' in number:
                number = number.split('+')[1]
            return number

        except ValueError:
            raise NotAuthenticated(
                "Invalid Token"
            )

    @staticmethod
    def get_data(token):
        try:
            decoded_token = auth.verify_id_token(token)
            return decoded_token

        except ValueError:
            raise NotAuthenticated(
                "No se encontro cuenta en Firebase o el token es invalido"
            )

    @staticmethod
    def send_push(notification_id, data, title, body):
        try:
            message = messaging.Message(
                data=data,
                token=notification_id,
                notification=messaging.Notification(
                    title=title,
                    body=body
                )
            )
            response = messaging.send(message)
        except Exception as e:
            pass

    @staticmethod
    def get_user(email):
        try:
            user = auth.get_user_by_email(email)
            return user
        except Exception as e:
            pass
