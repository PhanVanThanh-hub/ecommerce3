# Generated by Django 3.0 on 2021-05-29 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0035_delete_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=3),
        ),
    ]
