# Generated by Django 3.1.3 on 2021-05-04 19:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0010_auto_20210504_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_due_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 11, 19, 13, 23, 433191)),
        ),
    ]
