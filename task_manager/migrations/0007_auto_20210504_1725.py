# Generated by Django 3.1.3 on 2021-05-04 17:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0006_auto_20210504_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_due_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 11, 17, 25, 12, 532344)),
        ),
    ]
