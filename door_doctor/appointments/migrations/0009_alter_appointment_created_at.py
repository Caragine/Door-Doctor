# Generated by Django 4.1 on 2024-06-06 20:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0008_alter_appointment_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 6, 20, 42, 40, 10758, tzinfo=datetime.timezone.utc)),
        ),
    ]
