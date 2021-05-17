# Generated by Django 3.1 on 2021-04-24 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0016_order_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='discount',
            field=models.DecimalField(decimal_places=5, default=1.0, max_digits=8),
        ),
    ]
