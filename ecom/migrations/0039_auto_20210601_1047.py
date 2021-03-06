# Generated by Django 3.0 on 2021-06-01 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0038_delete_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='income',
            name='growth_cost',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='income',
            name='growth_revenue',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='income',
            name='growth_total_cost',
            field=models.FloatField(default=0.0, null=True),
        ),
    ]
