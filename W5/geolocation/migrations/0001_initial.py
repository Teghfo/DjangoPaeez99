# Generated by Django 3.1.2 on 2020-11-06 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('tehran', 'تهران'), ('alborz', 'البرز'), ('markazi', 'مرکزی')], max_length=20, verbose_name='استان')),
                ('city', models.CharField(max_length=50, verbose_name='شهر')),
                ('street', models.CharField(max_length=50, verbose_name='خیابان')),
                ('alley', models.CharField(max_length=50, verbose_name='کوچه')),
                ('number', models.CharField(max_length=50, verbose_name='پلاک')),
                ('poste_code', models.CharField(max_length=50, verbose_name='کدپستی')),
                ('priority_address', models.SmallIntegerField()),
                ('location', models.CharField(max_length=50, verbose_name='موقعیت جغرافیایی')),
            ],
        ),
    ]