from datetime import datetime
from django.shortcuts import render
import json
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from dateutil.parser import parse

from .models import User, Task, Project


def index(request):
    if request.user.is_authenticated:
        return render(request, "task_manager/index.html")
    else:
        return HttpResponseRedirect(reverse("login"))


def load_projects(request):
    if request.method == "GET":
        # query for preojects owned by the user
        projects = Project.objects.filter(user=request.user)
    return JsonResponse([project.serialize() for project in projects], safe=False)


def load_details(request, project_id):
    if request.method == "GET":
        # query for project based on model id

        project = Project.objects.get(id=project_id)
        tasks = Task.objects.filter(affiliated_project=project)
        return JsonResponse([task.serialize() for task in tasks], safe=False)


@csrf_exempt
def submit_project(request):
    if request.method == "POST":
        # add project
        data = json.loads(request.body)
        if data.get("title") is not None:
            title = data["title"]

            project = Project(
                project_title=title,
                user=request.user,
                project_start_time=datetime.now(),
                project_last_edited_time=datetime.now()
            )
            project.save()
            return JsonResponse({"Success": "project has been added"}, status=204)


@csrf_exempt
def mark_as_complete(request, task_id):
    if request.method == "PUT":
        # mark as complete
        try:
            task = Task.objects.get(pk=task_id)
            data = json.loads(request.body)
            if data.get("completed") is not None:
                task.completed = data["completed"]
            task.save()
            return HttpResponse(status=204)

        except Task.DoesNotExist:
            return JsonResponse({"error": "task not found."}, status=404)


@csrf_exempt
def reinstate_task(request, task_id):
    if request.method == "PUT":
        # mark as incompleted
        try:
            task = Task.objects.get(pk=task_id)
            data = json.loads(request.body)
            if data.get("completed") is not None:
                task.completed = data["completed"]
            task.save()
            return HttpResponse(status=204)
        except Task.DoesNotExist:
            return JsonResponse({"error": "task not found."}, status=404)


@csrf_exempt
def add_task(request, project_id):
    project = Project.objects.get(pk=project_id)
    if request.method == "POST":
        # add task
        data = json.loads(request.body)
        if data.get("task_name") is not None:
            task_name = data["task_name"]
        if data.get("task_description") is not None:
            task_description = data["task_description"]
        if data.get("task_due_date") is not None:
            task_due_date = parse(data["task_due_date"])

            task = Task(
                task_name=task_name,
                task_description=task_description,
                task_due_date=task_due_date,
                urgent=False,
                task_start_time=datetime.now(),
                user=request.user,
                affiliated_project=project
            )
            task.save()
            return JsonResponse({"Success": "task has been added"}, status=204)


@csrf_exempt
def delete_task(request, task_id):
    # query for requested task based on id
    if request.method == "DELETE":
        task = Task.objects.get(pk=task_id)
        task.delete()
    return JsonResponse({"Success": "task deleted"}, status=204)


@csrf_exempt
def delete_project(request, project_id):
    # query for requested project based on id
    if request.method == "DELETE":
        project = Project.objects.get(pk=project_id)
        project.delete()
    return JsonResponse({"Success": "project deleted"}, status=204)


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return render(request, "task_manager/index.html")
        else:
            return render(request, "task_manager/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "task_manager/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "task_manager/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "task_manager/register.html")
