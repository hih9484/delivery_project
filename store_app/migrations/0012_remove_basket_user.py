# Generated by Django 2.1.5 on 2019-02-01 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0011_basket_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='user',
        ),
    ]
