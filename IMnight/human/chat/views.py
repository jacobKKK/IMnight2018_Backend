# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from human.models import Relationship
from human.chat.serializers import MessageSerializer


class ChatView(ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = MessageSerializer

    def get_queryset(self):

        if 'label' not in self.kwargs:
            return []

        label = self.kwargs['label']
        try:
            room = Relationship.objects.get(label=label)
        except Relationship.DoesNotExist:
            print ("ws room does not exist label=%s", label)
            return []

        # We want to show the last 50 messages, ordered most-recent-last
        messages = reversed(room.messages.order_by('-timestamp')[:50])

        return messages
