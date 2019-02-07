# Generated by Django 2.1.5 on 2019-01-26 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0003_menu_price'),
        ('order_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='menu',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store_app.Menu'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='basket',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='basket',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
