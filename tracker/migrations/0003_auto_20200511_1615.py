# Generated by Django 3.0.6 on 2020-05-11 20:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20200511_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mealtime',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 11, 20, 15, 40, 392360, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sugarlevel',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 11, 20, 15, 40, 391920, tzinfo=utc)),
        ),
    ]