# Generated by Django 5.0 on 2024-04-11 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_remove_receipt_card_number_remove_receipt_cvv_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receipt',
            old_name='total_amount',
            new_name='total_price',
        ),
    ]
