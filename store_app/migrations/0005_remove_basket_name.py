# Generated by Django 2.1.5 on 2019-01-28 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0004_basket'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='name',
        ),
    ]
