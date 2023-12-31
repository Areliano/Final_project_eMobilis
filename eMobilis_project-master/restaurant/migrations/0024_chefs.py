# Generated by Django 3.2.23 on 2023-11-30 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0023_alter_stories_text1_alter_stories_text2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chefs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='chefs')),
                ('twitter', models.CharField(max_length=500)),
                ('facebook', models.CharField(max_length=500)),
                ('instagram', models.CharField(max_length=500)),
            ],
        ),
    ]
