from rest_framework import serializers
from django.conf import settings
from .models import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'




















# Create serializers here.

# class UserRegisterSerializer(serializers.ModelSerializer):
#
#     email = serializers.EmailField(required=True)
#     username = serializers.CharField(required=True)
#     password = serializers.CharField(min_length=8, write_only=True)
#
#     class Meta:
#         model = settings.AUTH_USER_MODEL
#         fields = ('email', 'user_name', 'first_name')
#         extra_kwargs = {'password': {'write_only': True}}