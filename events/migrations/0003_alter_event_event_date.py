# Generated by Django 3.2.13 on 2022-06-26 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_event_excerpt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.CharField(max_length=200),
        ),
    ]
