# Generated by Django 5.0.6 on 2024-06-02 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_servicecategory_service_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='brigade',
            name='categories',
            field=models.ManyToManyField(related_name='brigades', to='main.servicecategory', verbose_name='Категории'),
        ),
    ]
