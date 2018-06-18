# Generated by Django 2.0.4 on 2018-04-09 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0002_dormitory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.IntegerField()),
                ('status', models.BooleanField()),
                ('no_of_student', models.IntegerField()),
                ('hostel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostel.Hostel')),
            ],
        ),
    ]