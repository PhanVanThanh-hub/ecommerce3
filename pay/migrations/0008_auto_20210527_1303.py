# Generated by Django 3.0 on 2021-05-27 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0007_auto_20210527_1300'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discount20',
            old_name='dicount',
            new_name='discount',
        ),
        migrations.RenameField(
            model_name='discount30',
            old_name='dicount',
            new_name='discount',
        ),
        migrations.RenameField(
            model_name='discount50',
            old_name='dicount',
            new_name='discount',
        ),
    ]
