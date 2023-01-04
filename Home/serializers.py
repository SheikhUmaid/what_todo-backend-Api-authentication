from rest_framework import serializers
from .models import UserTodo
from django.contrib.auth.models import User




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]
    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTodo
        fields = ["id","todo", "completed"]

        
    def create(self, validated_data):
        todo = UserTodo.objects.create(
            user=self.context['request'].user,
            todo=validated_data['todo'],
            completed=validated_data['completed'])
        todo.save()
        return todo
    