# Generated by Django 3.1 on 2021-04-15 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0009_dataorder_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataorder',
            name='color',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='dataorder',
            name='size',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
