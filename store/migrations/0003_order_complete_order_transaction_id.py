# Generated by Django 4.1.4 on 2023-03-14 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0002_remove_order_complete_remove_order_transaction_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="complete",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="order",
            name="transaction_id",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
