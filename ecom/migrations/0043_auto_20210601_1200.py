# Generated by Django 3.0 on 2021-06-01 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0042_income_growth_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='income',
            old_name='growth_total',
            new_name='growth_total_cost',
        ),
        migrations.AddField(
            model_name='income',
            name='growth_total_profit',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='income',
            name='growth_total_revenue',
            field=models.FloatField(default=0.0, null=True),
        ),
    ]