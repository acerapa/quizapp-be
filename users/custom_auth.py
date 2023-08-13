from typing import Optional
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
import re

from django.contrib.auth.base_user import AbstractBaseUser

class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()

        pattern = r'^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w{2,3}$'
        user = None

        # use reqex to check for the validity of email in the username field
        if re.match(pattern, username) is not None:
            user = UserModel.objects.filter(email=username).first()
        else:
            user = UserModel.objects.filter(username=username).first()
        
        if user is None:
            return None
        
        if user.check_password(password):
            return user

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None        
