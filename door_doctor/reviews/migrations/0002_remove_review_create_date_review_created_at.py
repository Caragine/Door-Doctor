# Generated by Django 4.1 on 2024-05-25 23:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='create_date',
        ),
        migrations.AddField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 25, 23, 56, 20, 111925, tzinfo=datetime.timezone.utc)),
        ),
    ]
