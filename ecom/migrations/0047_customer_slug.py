# Generated by Django 3.0 on 2021-06-06 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0046_auto_20210606_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='slug',
            field=models.SlugField(default=1, max_length=2000),
            preserve_default=False,
        ),
    ]
