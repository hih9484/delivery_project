# Generated by Django 2.1.5 on 2019-01-30 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0006_basket_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='menu',
            field=models.CharField(max_length=50),
        ),
    ]
