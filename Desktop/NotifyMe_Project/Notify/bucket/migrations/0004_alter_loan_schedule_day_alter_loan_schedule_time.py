# Generated by Django 4.0.6 on 2023-05-24 07:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bucket', '0003_remove_insure_to_pay_insure_payment_intervel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='schedule_day',
            field=models.DateField(default=datetime.datetime(2023, 5, 1, 13, 11, 2, 749075)),
        ),
        migrations.AlterField(
            model_name='loan',
            name='schedule_time',
            field=models.TimeField(default=datetime.datetime(2023, 5, 24, 13, 11, 2, 749075)),
        ),
    ]
