# Generated by Django 3.1 on 2021-04-13 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0004_favoriteproduct_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favoriteproduct',
            name='customer',
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecom.customer')),
            ],
        ),
        migrations.AddField(
            model_name='favoriteproduct',
            name='favorite',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecom.favorite'),
        ),
    ]
