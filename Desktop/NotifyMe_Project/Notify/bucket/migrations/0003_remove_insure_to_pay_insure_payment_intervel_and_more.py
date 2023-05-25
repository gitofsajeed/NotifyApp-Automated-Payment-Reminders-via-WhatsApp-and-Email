# Generated by Django 4.0.6 on 2023-05-24 06:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bucket', '0002_rent_loan_schedule_day_loan_schedule_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='insure',
            name='to_pay',
        ),
        migrations.AddField(
            model_name='insure',
            name='payment_intervel',
            field=models.CharField(choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Yearly', 'Yearly')], default='Yearly', max_length=20),
        ),
        migrations.AlterField(
            model_name='loan',
            name='payment_period',
            field=models.CharField(choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Yearly', 'Yearly')], default='Monthly', max_length=20),
        ),
        migrations.AlterField(
            model_name='loan',
            name='schedule_day',
            field=models.DateField(default=datetime.datetime(2023, 5, 1, 11, 49, 48, 380809)),
        ),
        migrations.AlterField(
            model_name='loan',
            name='schedule_time',
            field=models.TimeField(default=datetime.datetime(2023, 5, 24, 11, 49, 48, 380808)),
        ),
    ]
