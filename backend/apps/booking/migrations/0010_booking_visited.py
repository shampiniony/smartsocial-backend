# Generated by Django 5.0.6 on 2024-06-15 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0009_alter_buyer_email_alter_cartticket_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='visited',
            field=models.BooleanField(default=False),
        ),
    ]
