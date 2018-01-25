from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from rest_framework import status
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.schemas import AutoSchema
import coreapi

from lottery.models import Task, ProgressTask
from lottery.serializers import RewardSerializer

import logging
testlog = logging.getLogger('testdevelop')


class ProgressTaskView(ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = RewardSerializer()

    def get_queryset(self):
        user = self.request.user

        queryset = ProgressTask.objects.get_progress_task(user)
        return queryset


@api_view(['POST'])
def finish_task(request):
    if ('label' in request.data):
        try:
            finished_task = ProgressTask.objects.finish_task_by_label(
                request.user, request.data['label'])
            if finished_task is not None:
                return Response({"message": "Task finished Succeesslly"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "Task already finished or closed"}, status=status.HTTP_201_CREATED)

        except Exception as error:
            return Response({"message": "this task label dosen't exist"}, status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response({"message": "parameter \'label\' not in scoope"}, status=status.HTTP_400_BAD_REQUEST)
