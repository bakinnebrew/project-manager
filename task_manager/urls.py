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
         views.load_details, name="load_details"),
    path("submit_project", views.submit_project, name="subimt_barrel"),
    path("add_task/<int:project_id>", views.add_task, name="add_task"),
    path("delete_task/<int:task_id>", views.delete_task, name="delete_task"),
    path("delete_project/<int:project_id>",
         views.delete_project, name="delete_project"),
    path("mark_as_complete/<int:task_id>",
         views.mark_as_complete, name="mark_as_complete"),
    path("reinstate_task/<int:task_id>",
         views.reinstate_task, name="reinstate_task"),
    path("edit_project/<int:project_id>",
         views.edit_project, name="edit_project"),
    path("read_alerts", views.read_alerts, name="read_alerts"),
    # path("load_count/<int:project_id>", views.load_count, name="load_count")
]
