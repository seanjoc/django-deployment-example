# Generated by Django 2.2.1 on 2019-08-31 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forth_app', '0002_auto_20190831_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ufirst_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='ulast_name',
            field=models.CharField(max_length=100),
        ),
    ]
