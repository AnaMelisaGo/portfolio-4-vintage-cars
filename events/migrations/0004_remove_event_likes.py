# Generated by Django 3.2.13 on 2022-06-27 02:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_event_event_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='likes',
        ),
    ]