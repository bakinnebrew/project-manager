# Generated by Django 3.1.3 on 2021-05-04 18:59

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0007_auto_20210504_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='affiliated_project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_manager.project'),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_due_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 11, 18, 59, 3, 529136)),
        ),
    ]
