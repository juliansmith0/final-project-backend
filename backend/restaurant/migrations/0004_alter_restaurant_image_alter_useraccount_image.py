# Generated by Django 4.0.4 on 2022-04-27 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_alter_restaurant_name_alter_useraccount_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='image',
            field=models.CharField(blank=True, default='', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='image',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
