# Generated by Django 3.1.2 on 2020-11-21 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0009_account_product_supplier'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='menucat',
            constraint=models.UniqueConstraint(fields=('name', 'element'), name='menu cat constraint'),
        ),
    ]