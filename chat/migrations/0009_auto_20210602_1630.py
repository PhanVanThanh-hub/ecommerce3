# Generated by Django 3.0 on 2021-06-02 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0008_auto_20210601_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='content',
            field=models.CharField(default='No Message', editable=False, max_length=100000),
        ),
        migrations.AddField(
            model_name='room',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
