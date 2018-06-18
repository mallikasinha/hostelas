# Generated by Django 2.0.4 on 2018-04-21 17:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0016_auto_20180421_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dormitory',
            name='hostel',
            field=models.OneToOneField(blank=True, default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='hostel.Hostel'),
            preserve_default=False,
        ),
    ]
