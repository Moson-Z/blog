# Generated by Django 2.2.3 on 2020-04-26 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200414_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='num',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
