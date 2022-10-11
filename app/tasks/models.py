from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Task(models.Model):
    body = models.TextField()
    date = models.DateField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        name = f"{self.user}-{self.date}-{self.body[:10]}..."
        return name

    class Meta:
        ordering = ["date"]
