# Generated by Django 3.1.2 on 2020-12-25 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pooldar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aghazadeh', models.CharField(default='m.r', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='publication',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.pooldar'),
        ),
    ]