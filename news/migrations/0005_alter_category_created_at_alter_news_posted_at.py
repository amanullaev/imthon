# Generated by Django 4.2.4 on 2023-08-15 12:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_category_created_at_alter_news_posted_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 15, 17, 16, 0, 826983)),
        ),
        migrations.AlterField(
            model_name='news',
            name='posted_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 15, 17, 16, 0, 999041)),
        ),
    ]
