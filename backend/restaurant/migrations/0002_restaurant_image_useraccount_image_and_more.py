# Generated by Django 4.0.4 on 2022-04-27 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='image',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='image',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.TextField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='name',
            field=models.CharField(default='name', max_length=255),
        ),
    ]
