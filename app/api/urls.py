from django.urls import path
from tasks.views import TaskList

app_name = 'api'

urlpatterns = [
    path('tasks/v1.0/', TaskList.as_view(), name='task_list'),
]
