# Generated by Django 4.0.4 on 2022-04-29 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_restaurant_cuisine_restaurant_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(blank=True, default='', max_length=5000, null=True),
        ),
    ]