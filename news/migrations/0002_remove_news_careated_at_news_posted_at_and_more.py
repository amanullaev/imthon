# Generated by Django 4.2.4 on 2023-08-15 11:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='careated_at',
        ),
        migrations.AddField(
            model_name='news',
            name='posted_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 15, 16, 40, 45, 655691)),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 15, 16, 40, 45, 483813)),
        ),
    ]
