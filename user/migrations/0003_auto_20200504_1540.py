# Generated by Django 2.2.3 on 2020-05-04 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200504_1149'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='password',
            new_name='set_password',
        ),
    ]
