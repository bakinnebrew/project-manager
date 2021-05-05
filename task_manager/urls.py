from django.urls import path

from . import views

app_name = "task_manager"
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    # API Routes
    path("load_projects", views.load_projects, name="load_projects"),
    path("load_details/<int:project_id>",
         views.load_details, name="load_details")
]
