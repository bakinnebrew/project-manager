from django.contrib import admin

from django.contrib import admin

# Register your models here.
from .models import User, Task, Project, Alert

admin.site.register(User)
admin.site.register(Task)
admin.site.register(Project)
admin.site.register(Alert)
