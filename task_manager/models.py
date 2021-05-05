from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime, timedelta


class User(AbstractUser):
    pass


class Project(models.Model):
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="owners")
    project_title = models.TextField(max_length=64, blank=True)
    project_start_time = models.DateTimeField(auto_now_add=True)
    project_last_edited_time = models.DateTimeField(auto_now=True)

    def serialize(self):
        return {
            "id": self.id,
            "owner_id": self.user.id,
            "owner": self.user.username,
            "title": self.project_title,
            "start_timestamp": self.project_start_time.strftime("%b %-d %Y, %-I:%M %p"),
            "last_edit_timestamp": self.project_last_edited_time.strftime("%b %-d %Y, %-I:%M %p"),
        }


class Task(models.Model):
    affiliated_project = models.ForeignKey(
        "Project", on_delete=models.CASCADE)
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="task_managers")
    task_name = models.TextField(max_length=64)
    task_description = models.TextField(max_length=132)
    task_start_time = models.DateTimeField(auto_now_add=True)
    task_due_date = models.DateTimeField(
        default=datetime.now()+timedelta(days=7))
    urgent = models.BooleanField(default=False)

    def serialize(self):
        return{
            "id": self.id,
            "affiliated_project": self.affiliated_project.project_title,
            "affiliated_project_id": self.affiliated_project.id,
            "task_author": self.user.id,
            "task_name": self.task_name,
            "task_description": self.task_description,
            "task_start_time": self.task_start_time,
            "task_due_date": self.task_due_date,
            "urgent": self.urgent
        }
