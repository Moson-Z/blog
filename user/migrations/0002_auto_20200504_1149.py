# Generated by Django 2.2.3 on 2020-05-04 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.IntegerField(max_length=20, null=True, verbose_name='手机'),
        ),
    ]
