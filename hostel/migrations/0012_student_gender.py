# Generated by Django 2.0.4 on 2018-04-18 18:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0011_auto_20180414_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]
