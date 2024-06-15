# Generated by Django 5.0.6 on 2024-06-15 01:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_remove_booking_file'),
        ('core', '0007_remove_place_images_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartticket',
            name='event',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='core.event'),
            preserve_default=False,
        ),
    ]