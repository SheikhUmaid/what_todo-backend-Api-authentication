
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from Home import models
from .serializers import TodoSerializer
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

#API VIEW


class TodoView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        todos = models.UserTodo.objects.filter(user = request.user).all().order_by('-created_at')
        # todos = models.UserTodo.objects.all()
        serialized = TodoSerializer(todos, many=True)
        print(serialized.data)
        return Response(serialized.data)
    
    
    def post(self, request):
        serializer = TodoSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Todo Created'})
        else:
            return Response({'message': 'Todo not Created'})
    
    


class deleteView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, id):
        models.UserTodo.objects.get(id=id).delete()
        return Response({'message': 'Todo Deleted'})


    def delete(self, request, id):
        models.UserTodo.objects.get(id=id).delete()
        return Response({'message': 'Todo Deleted'})    





class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=serializer.data['username'])
            token,_ = Token.objects.get_or_create(user=user)
            return Response({'message': 'User Created', 'token': token.key, 'username': user.username})
        else:
            return Response({'message': 'User not Created'})

class LoginView(APIView):

    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            token,_ = Token.objects.get_or_create(user=user)
            return Response({'message': 'User Logged In', 'token': token.key, 'username': user.username})
        else:
            return Response({'message': 'User not Logged In'})






















#WEB VIEW
@login_required(login_url='login')
def index_view(request):
    todos = models.UserTodo.objects.filter(user = request.user).all().order_by('-created_at')
    if request.method == "POST":
        todo = request.POST.get('todo')
        models.UserTodo.objects.create(user= request.user, todo= todo).save()
        print('saved')

    return render(request, 'index.html', {'todos': todos})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    # print(request.user.username)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("login successful")
            return redirect('index')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')



def delete_view(request, id):
    models.UserTodo.objects.get(id=id).delete()
    messages.success(request, 'Todo Deleted')
    return redirect('index', )
# 
#D9Ax43Uzvb7P4*



@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')



