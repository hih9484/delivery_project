# Generated by Django 2.1.5 on 2019-01-15 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board_app', '0002_auto_20190110_0420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boarddb',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
