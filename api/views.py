from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Task, Users
from .serializers import TaskSerializer, UserSerializer


class TaskView(APIView):
    def get(self, request):
        items = Task.objects.all()
        serializer = TaskSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def put(self, request):
        task = Task.objects.get(id=request.data["id"])
        task.title = request.data["title"]
        task.description = request.data["description"]
        task.status = request.data["status"]
        task.due_date = request.data["due_date"]
        task.save()
        return Response(request.data, status=201)
    
    def delete(self, request):
        task = Task.objects.get(id=request.data["id"])
        task.delete()
        return Response(request.data, status=201)

class UserView(APIView):
    def post(self, request):
        try:
            Users.objects.get(userName = request.data["userName"], password = request.data["password"])
            return Response("Acceso Exitoso", status=200)
        except:
            return Response("Credenciales Incorrectas", status=401)

    def get(self, request):
        items = Users.objects.all()
        serializer = UserSerializer(items, many=True)
        return Response(serializer.data)
        