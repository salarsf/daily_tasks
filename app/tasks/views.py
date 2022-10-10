from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
import datetime
from .models import Task
from .serializers import TaskSerializer


# Create your views here.


class TaskList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        tasks = Task.objects.filter(user=request.user).all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodayTask(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        today = datetime.date.today()
        tasks = Task.objects.filter(user=request.user, date=today)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
