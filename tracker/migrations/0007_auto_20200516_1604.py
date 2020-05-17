# Generated by Django 3.0.6 on 2020-05-16 20:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0006_auto_20200514_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mealtime',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 16, 20, 4, 54, 500641, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sugarlevel',
            name='sugar_level',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='sugarlevel',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 16, 20, 4, 54, 500200, tzinfo=utc)),
        ),
    ]