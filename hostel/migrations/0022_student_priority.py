# Generated by Django 2.0.4 on 2018-04-21 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0021_remove_student_priority_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='priority',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
