# Generated by Django 2.0.1 on 2018-05-07 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_listwish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listwish',
            name='date',
        ),
    ]