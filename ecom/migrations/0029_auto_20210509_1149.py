# Generated by Django 3.0 on 2021-05-09 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0028_loginattempts'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='amout',
            field=models.IntegerField(blank=True, default=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=30.0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='loginattempts',
            name='end',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='loginattempts',
            name='start',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
