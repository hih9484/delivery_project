# Generated by Django 2.1.5 on 2019-01-10 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoardDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=30)),
                ('context', models.TextField()),
                ('create_date', models.DateTimeField()),
                ('update_date', models.DateTimeField()),
                ('view_count', models.IntegerField()),
                ('good_count', models.IntegerField()),
                ('bad_count', models.IntegerField()),
            ],
        ),
    ]
