# Generated by Django 3.0 on 2021-05-27 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0005_auto_20210527_1239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discount',
            name='discount20',
        ),
        migrations.AddField(
            model_name='discount',
            name='discount20',
            field=models.ManyToManyField(blank=True, to='pay.Discount20'),
        ),
        migrations.RemoveField(
            model_name='discount',
            name='discount30',
        ),
        migrations.AddField(
            model_name='discount',
            name='discount30',
            field=models.ManyToManyField(blank=True, to='pay.Discount30'),
        ),
        migrations.RemoveField(
            model_name='discount',
            name='discount50',
        ),
        migrations.AddField(
            model_name='discount',
            name='discount50',
            field=models.ManyToManyField(blank=True, to='pay.Discount50'),
        ),
    ]
