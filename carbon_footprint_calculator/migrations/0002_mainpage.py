# Generated by Django 3.0.2 on 2020-01-29 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carbon_footprint_calculator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('information', models.TextField()),
            ],
        ),
    ]