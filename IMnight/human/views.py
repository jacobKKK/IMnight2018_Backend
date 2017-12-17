from django.contrib.auth import get_user_model

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.schemas import AutoSchema
import coreapi

from human.models import User
from human.serializers import UserDetailsSerializer

UserModel = get_user_model()


class UserDetailsView(generics.RetrieveUpdateAPIView):
    """

    get:
    Display fields: pk, username, email, first_name, last_name

    retrieve:
    Accepted fields: username, first_name, last_name

    Read-only fields: pk, email

    Returns UserModel fields.
    """

    serializer_class = UserDetailsSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

    def get_queryset(self):
        """
        Adding this method since it is sometimes called when using
        django-rest-swagger
        https://github.com/Tivix/django-rest-auth/issues/275
        """
        return UserModel.objects.none()
