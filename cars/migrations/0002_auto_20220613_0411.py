# Generated by Django 3.2.13 on 2022-06-13 04:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcar',
            name='can_rent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='postcar',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='postcar',
            name='year_manufactured',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1875), django.core.validators.MaxValueValidator(2000)]),
        ),
    ]
