from django.contrib.auth.hashers import make_password
from rest_framework.utils import json
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from rest_framework_simplejwt.tokens import RefreshToken

# from django.contrib.auth.models import User
# from django.contrib.auth.base_user import BaseUserManager

from Auth.models import NewUser, CustomAccountManager



class GoogleView(APIView):
    def post(self, request):
        payload = {'access_token': request.data.get("token")}  # validate the token
        r = requests.get('https://www.googleapis.com/oauth2/v2/userinfo', params=payload)
        data = json.loads(r.text)

        if 'error' in data:
            content = {'message': 'wrong google token / this google token is already expired.'}
            return Response(content)
        # create user if not exist
        try:
            user = NewUser.objects.get(email=data['email'])
        except NewUser.DoesNotExist:
            user = NewUser()
            user.username = data['email']
            # provider random default password
            user.password = make_password(CustomAccountManager().make_random_password())
            user.email = data['email']
            user.save()

        token = RefreshToken.for_user(user)  # generate token without username & password
        response = {}
        response['username'] = user.user_name
        response['access_token'] = str(token.access_token)
        response['refresh_token'] = str(token)
        return Response(response)
