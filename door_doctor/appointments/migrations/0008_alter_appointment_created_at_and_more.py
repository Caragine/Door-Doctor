# Generated by Django 4.1 on 2024-06-06 20:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0007_alter_appointment_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 6, 20, 29, 16, 435208, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='phone_number',
            field=models.CharField(max_length=15, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='reason_for_appointment',
            field=models.TextField(verbose_name='Reason For Appointment'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='state',
            field=models.CharField(default='NY', max_length=2),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='zip_code',
            field=models.CharField(max_length=10, null=True, verbose_name='Zip Code'),
        ),
    ]
