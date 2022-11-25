from django.db import models
from django.contrib.auth import get_user_model
import datetime

# Create your models here.

User = get_user_model()


class TaskManager(models.Manager):
    def get_todays_tasks_for_user(self, user):
        today = datetime.date.today()
        return self.get_queryset().filter(user=user, date=today)


class Task(models.Model):
    body = models.TextField()
    date = models.DateField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    objects = TaskManager()

    def __str__(self):
        name = f"{self.user}-{self.date}-{self.body[:10]}..."
        return name

    class Meta:
        ordering = ["date"]
