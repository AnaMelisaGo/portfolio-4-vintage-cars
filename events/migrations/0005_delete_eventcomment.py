# Generated by Django 3.2.13 on 2022-06-28 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_remove_event_likes'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EventComment',
        ),
    ]