# Generated by Django 2.1.5 on 2019-01-28 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0005_remove_basket_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
