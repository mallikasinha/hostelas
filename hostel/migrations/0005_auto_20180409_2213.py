# Generated by Django 2.0.4 on 2018-04-09 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0004_room_room_no'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hostel',
            old_name='available_room',
            new_name='available_rooms',
        ),
        migrations.RemoveField(
            model_name='room',
            name='no_of_student',
        ),
    ]
