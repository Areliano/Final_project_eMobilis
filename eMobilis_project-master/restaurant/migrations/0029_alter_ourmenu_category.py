# Generated by Django 4.2.7 on 2023-11-30 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0028_homepage_btn2_homepage_description2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourmenu',
            name='category',
            field=models.CharField(choices=[('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('dinner', 'Dinner'), ('Dessert', 'Dessert'), ('Winecard', 'Winecard'), ('Drinks', 'Drinks')], default='Dinner', max_length=50),
        ),
    ]
