# Generated by Django 4.2 on 2023-04-19 19:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Youtubers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('photo', models.ImageField(upload_to='media/ytubers/%y/%m')),
                ('video_url', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('city', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('heigth', models.IntegerField()),
                ('crew', models.CharField(max_length=255)),
                ('camera_type', models.CharField(max_length=255)),
                ('subs_count', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('is_featured', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]