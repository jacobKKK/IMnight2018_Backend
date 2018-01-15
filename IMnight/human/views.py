from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from rest_framework import status
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.schemas import AutoSchema
import coreapi

from human.models import Relationship
from human.serializers import UserDetailsSerializer, RelationshipSerializer


UserModel = get_user_model()


class SelfDetailsView(RetrieveUpdateAPIView):
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


class UserDetailsView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserDetailsSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = User.objects.all()
        if 'username' in self.kwargs:
            username = self.kwargs['username']
            queryset = queryset.filter(username=username)
        return queryset


class RelationshipDetailsView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RelationshipSerializer

    def get_queryset(self):
        user = self.request.user

        queryset = Relationship.objects.get_performers(user)

        return queryset


class DailyPerformerView(ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = RelationshipSerializer

    def get_queryset(self):
        user = self.request.user

        queryset = Relationship.objects.get_daily(user)
        return queryset
