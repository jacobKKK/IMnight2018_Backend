# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from earth.models import HoldingVocher, Store, Vocher
from earth.serializers import HoldingVocherSerializer, VocherSerializer


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
    取得某特定用戶資料（Include Profile）
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
