# Generated by Django 5.0.6 on 2024-06-01 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_alter_memberbrigade_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='memberbrigade',
            name='experience',
            field=models.IntegerField(default=1, verbose_name='Опыт'),
        ),
    ]
