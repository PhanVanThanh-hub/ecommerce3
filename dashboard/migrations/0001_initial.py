# Generated by Django 3.0 on 2021-05-30 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='giftVoucher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amout50', models.IntegerField(blank=True, null=True)),
                ('amout30', models.IntegerField(blank=True, null=True)),
                ('amout20', models.IntegerField(blank=True, null=True)),
                ('dateTimeGift', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]