from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer

# Create your views here.


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def task_list_get_all_or_create(request):
    if request.method == "GET":
        tasks = Task.objects.all()
        serializer = TaskSerializer(
            tasks, many=True
        )  # many= True when multiple instance present
        return Response(serializer.data, status=200)
    elif request.method == "POST":
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def task_retrieve_update_destroy(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response({"error": "Task not found"}, status=404)

    if request.method == "GET":
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=200)
    elif request.method == "PUT":
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    elif request.method == "DELETE":
        task.delete()
        return Response(status=204)
