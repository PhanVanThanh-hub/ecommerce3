# Generated by Django 3.0 on 2021-05-30 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('data_ordered', models.DateTimeField(auto_now_add=True)),
                ('tag', models.CharField(choices=[('Streetstlye', 'Streetstlye'), ('Craft', 'Craft'), ('Fashion', 'Fashion'), ('Denim', 'Denim'), ('Lifestyle', 'Lifestyle')], max_length=200, null=True)),
                ('categories', models.CharField(choices=[('Fashion', 'Fashion'), ('Beauty', 'Beauty'), ('Streetstlye', 'Streetstlye'), ('Lifestyle', 'Lifestyle'), ('DIY&Craft', 'DIY&Craft')], default='null', max_length=200, null=True)),
                ('images1', models.ImageField(blank=True, default='null', null=True, upload_to='')),
                ('detail', models.CharField(max_length=1000, null=True)),
                ('detail1', models.CharField(max_length=10000, null=True)),
            ],
        ),
    ]
