# Generated by Django 4.0.4 on 2022-04-27 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_alter_restaurant_image_alter_useraccount_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='cuisine',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='price',
            field=models.CharField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4)], default='', max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='location',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='image',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='image',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
    ]