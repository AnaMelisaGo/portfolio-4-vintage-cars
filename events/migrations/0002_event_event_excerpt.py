# Generated by Django 3.2.13 on 2022-06-26 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_excerpt',
            field=models.TextField(default='Short text about the event'),
        ),
    ]
