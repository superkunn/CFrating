# Generated by Django 2.1.3 on 2018-11-14 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contest',
            name='start_time',
        ),
        migrations.AlterField(
            model_name='student',
            name='cf_rating',
            field=models.IntegerField(default=0),
        ),
    ]
