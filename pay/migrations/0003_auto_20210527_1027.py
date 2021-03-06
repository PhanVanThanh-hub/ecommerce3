# Generated by Django 3.0 on 2021-05-27 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0035_delete_discount'),
        ('pay', '0002_auto_20210527_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='discount', to='ecom.Customer'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='discount20',
            field=models.ManyToManyField(blank=True, to='pay.Discount20'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='discount30',
            field=models.ManyToManyField(blank=True, to='pay.Discount30'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='discount50',
            field=models.ManyToManyField(blank=True, to='pay.Discount50'),
        ),
    ]
