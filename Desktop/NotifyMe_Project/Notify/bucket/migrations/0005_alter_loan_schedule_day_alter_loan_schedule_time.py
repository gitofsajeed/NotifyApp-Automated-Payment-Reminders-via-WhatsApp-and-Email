# Generated by Django 4.0.6 on 2023-05-24 07:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bucket', '0004_alter_loan_schedule_day_alter_loan_schedule_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='schedule_day',
            field=models.DateField(default=datetime.datetime(2023, 5, 1, 13, 17, 42, 276366)),
        ),
        migrations.AlterField(
            model_name='loan',
            name='schedule_time',
            field=models.TimeField(default=datetime.datetime(2023, 5, 24, 13, 17, 42, 276366)),
        ),
    ]
