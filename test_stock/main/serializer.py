from rest_framework import serializers
from main.models import UserInfo

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['user_name','job_title','salary','city','required_experience']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['id', 'user_name','job_title','salary','city','required_experience','request_date']