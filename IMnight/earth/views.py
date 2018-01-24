# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from earth.models import HoldingVocher, Store, Vocher
from earth.serializers import HoldingVocherSerializer, VocherSerializer, UseVocherSerializer


@api_view(['POST'])
def hello_world(request):
    if ('label' in request.data):
        if HoldingVocher.objects.used_vocher(request.user, request.data['label']):
            return Response("Used Succeesslly", status=status.HTTP_201_CREATED)
        else:
            return Response("Error occured when vocher used", status=HTTP_406_NOT_ACCEPTABLE)
    else:
        return Response("parameter \'lable\' not in scoope", status=status.HTTP_400_BAD_REQUEST)


class DailyVocherView(ListAPIView):
    """
    取得當日的daily vocher
    """
    permission_classes = (IsAuthenticated, )
    serializer_class = HoldingVocherSerializer

    def get_queryset(self):
        user = self.request.user

        queryset = HoldingVocher.objects.get_daily(user)
        return queryset


class StoreVocherView(ListAPIView):
    """
    取得用戶的Vocher
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = VocherSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `storename` query parameter in the URL.
        """
        user = self.request.user
        if 'storename' in self.kwargs:
            storename = self.kwargs['storename']
            queryset = HoldingVocher.objects.get_vochers(user, storename)
        else:
            queryset = HoldingVocher.objects.get_vochers(user)
        return queryset
