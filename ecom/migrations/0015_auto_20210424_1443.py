# Generated by Django 3.1 on 2021-04-24 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0014_order_discount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='discount',
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount50', models.CharField(max_length=10, null=True)),
                ('complete', models.BooleanField(default=False)),
                ('customer', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecom.customer')),
            ],
        ),
    ]
