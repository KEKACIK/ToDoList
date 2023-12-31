# Generated by Django 4.2.2 on 2023-06-18 20:29

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admin_web', '0006_task_close'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.CreateModel(
            name='Telegram',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('telegram_id', models.CharField(max_length=64, verbose_name='ID Телеграм')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, verbose_name='Время создания')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Телеграм',
                'verbose_name_plural': 'Телеграммы',
                'db_table': 'telegrams',
            },
        ),
    ]
