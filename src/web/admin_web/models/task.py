from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    class Meta:
        db_table = 'tasks'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    id = models.AutoField(primary_key=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    title = models.CharField(max_length=64, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    close = models.BooleanField(default=False, verbose_name="Завершена")

    created_at = models.DateTimeField(default=datetime.now, verbose_name="Время создания")

    def __str__(self):
        return f"{self.id} - {self.title}"
