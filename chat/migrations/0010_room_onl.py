# Generated by Django 3.0 on 2021-06-03 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0009_auto_20210602_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='onl',
            field=models.BooleanField(default=False),
        ),
    ]
