# Generated by Django 3.1.2 on 2020-11-19 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_element_descriptions'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'کتگوری'},
        ),
        migrations.AddField(
            model_name='element',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]