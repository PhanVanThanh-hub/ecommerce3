# Generated by Django 3.1 on 2021-04-13 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0003_remove_favoriteproduct_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='favoriteproduct',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecom.customer'),
        ),
    ]
