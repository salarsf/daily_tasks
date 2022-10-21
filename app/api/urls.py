from django.urls import path
from tasks.views import TaskList, TodayTask, TaskEdit

app_name = 'api'

urlpatterns = [
    path('tasks/v1.0/', TaskList.as_view(), name='task_list'),
    path('tasks/v1.0/edit/<pk>', TaskEdit.as_view(), name='task_edit'),
    path('tasks/v1.0/today', TodayTask.as_view(), name='today_task_list'),
]
