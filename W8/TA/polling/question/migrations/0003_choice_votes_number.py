# Generated by Django 3.1.4 on 2020-12-23 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_auto_20201223_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='votes_number',
            field=models.IntegerField(default=0),
        ),
    ]
