# Generated by Django 5.0.6 on 2024-06-05 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0035_schedulemember_service_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicerequest',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес'),
        ),
    ]