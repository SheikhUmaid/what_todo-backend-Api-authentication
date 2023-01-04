from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.


class UserTodo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.todo
