# Generated by Django 5.0.4 on 2024-04-07 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_status_message_remove_status_status_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicerequest',
            name='card_number',
            field=models.CharField(default=0, max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='cvv',
            field=models.CharField(default=1, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='expiry_date',
            field=models.CharField(default=1, max_length=7),
            preserve_default=False,
        ),
    ]
