# Generated by Django 3.1.3 on 2021-05-03 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0002_project_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='user',
            new_name='owner',
        ),
    ]