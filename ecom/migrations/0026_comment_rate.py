# Generated by Django 3.1 on 2021-05-06 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0025_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='rate',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=3),
        ),
    ]
