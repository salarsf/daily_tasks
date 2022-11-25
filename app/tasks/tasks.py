from celery import shared_task
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string
from django.core.mail import send_mail
from .models import Task

User = get_user_model()


@shared_task
def send_daily_mails():
    for user in User.objects.all():
        tasks = Task.objects.get_todays_tasks_for_user(user)
        if tasks:
            mail_context = {
                "user": user,
                "tasks": tasks
            }

            mail_body = render_to_string('email/base_daily_tasks.html', mail_context)

            send_mail(
                'Your tasks for the day',
                mail_body,
                'salar.develope@gmail.com',
                [user.email],
                html_message=mail_body
            )
            print(f"email for {user} is sent")
        else:
            print(f"user {user}: has no tasks today")
