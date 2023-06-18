from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Telegram(models.Model):
    class Meta:
        db_table = 'telegrams'
        verbose_name = 'Телеграм'
        verbose_name_plural = 'Телеграммы'

    id = models.AutoField(primary_key=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    telegram_id = models.CharField(max_length=64, verbose_name="ID Телеграм")

    created_at = models.DateTimeField(default=datetime.now, verbose_name="Время создания")

    def __str__(self):
        return f"{self.id} - {self.telegram_id}"
