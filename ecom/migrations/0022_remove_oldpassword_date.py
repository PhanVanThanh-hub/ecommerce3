# Generated by Django 3.1 on 2021-05-01 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0021_oldpassword'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oldpassword',
            name='date',
        ),
    ]