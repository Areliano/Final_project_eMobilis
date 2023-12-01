# Generated by Django 4.2.7 on 2023-11-29 10:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0018_remove_homepage_image1_remove_homepage_image2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='time',
        ),
        migrations.AlterField(
            model_name='customer',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
