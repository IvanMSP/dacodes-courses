# Django

# Third-party Libraries
from rest_framework import status
from rest_framework.views import APIView

# Owner
from .serializers import UserBaseSerializer
from ...models import User
from ...firebase import FirebaseHelper
from ...helpers.users import get_username
from dacodes_framework.response import EnvelopeErrorResponse, EnvelopeResponse
from reusable.constants import NULL_VALUE


class UserAuthToken(APIView):
    """
        A view to login or create a user instance
    """
    authentication_classes = []

    def post(self, request):
        token = request.META.get('HTTP_AUTHORIZATION', None)
        if token in NULL_VALUE:
            return EnvelopeErrorResponse('TOKEN_MUST_BE_PROVIDED', status=status.HTTP_400_BAD_REQUEST)
        data = FirebaseHelper.get_token(token)
        email = data.get('email')
        username = get_username(email)
        user_type = request.POST.get('userType', 'student')
        user, created =  User.objects.get_or_create(email=email)
        if created is True:
            response_status = status.HTTP_201_CREATED
            user.username = username
            user.email = email
            user.set_user_type(user_type)
        else:
            response_status = status.HTTP_200_OK
        serializer = UserBaseSerializer(user)
        user.save()
        return EnvelopeResponse(serializer.data, status=response_status)