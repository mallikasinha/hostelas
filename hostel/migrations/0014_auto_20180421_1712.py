# Generated by Django 2.0.4 on 2018-04-21 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0013_auto_20180421_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dormitory',
            name='hostel',
            field=models.OneToOneField(unique=True, on_delete=django.db.models.deletion.CASCADE, to='hostel.Hostel'),
        ),
    ]
