# Generated by Django 3.0 on 2021-05-31 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20210530_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='giftvoucher',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
