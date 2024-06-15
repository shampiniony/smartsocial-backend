# Generated by Django 5.0.6 on 2024-06-15 18:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0010_booking_visited'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='quantity',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
    ]