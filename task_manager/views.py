from django.shortcuts import render
import json
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.db import IntegrityError

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
