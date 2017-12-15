from django.db import models

from django.conf import settings

from rest_framework.authtoken.models import Token as DefaultTokenModel

# Register your models here.

TokenModel = DefaultTokenModel
