# Thirdy Party Libraries
from rest_framework import serializers
from rest_framework.authtoken.models import Token

# Owner
from accounts.models import User


class UserBaseSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    userType = serializers.CharField(source='user_type')

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'token',
            'userType',
        ]

    def get_token(self, user):
        token, created = Token.objects.get_or_create(user=user)
        if created is False:
            token.delete()
            token = Token.objects.create(user=user)
        return token.key 
    

class TeacherSerializer(serializers.ModelSerializer):
    fullName = serializers.CharField(source='get_full_name')
    isTeacher = serializers.BooleanField(source='is_teacher')

    class Meta:
        model = User
        fields = (
            'id',
            'fullName',
            'isTeacher',
        )