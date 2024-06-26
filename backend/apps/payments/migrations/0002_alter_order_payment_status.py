# Generated by Django 5.0.6 on 2024-06-12 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payments", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="payment_status",
            field=models.CharField(
                choices=[
                    ("pending", "Ожидание оплаты"),
                    ("waiting_for_capture", "Платеж оплачен, ожидают списания"),
                    ("succeeded", "Платеж успешно завершен"),
                    ("canceled", "Платеж отменен"),
                ],
                default="pending",
                max_length=20,
            ),
        ),
    ]
