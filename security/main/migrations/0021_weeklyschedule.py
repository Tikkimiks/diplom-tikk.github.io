# Generated by Django 5.0 on 2024-04-16 11:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_schedule_work_days'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WeeklySchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='Начало недели')),
                ('end_date', models.DateField(verbose_name='Конец недели')),
                ('task_description', models.TextField(verbose_name='Описание задачи')),
                ('assigned_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Назначенный работник')),
                ('brigade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.brigade', verbose_name='Бригада')),
            ],
            options={
                'verbose_name': 'Недельное расписание',
                'verbose_name_plural': 'Недельные расписания',
            },
        ),
    ]