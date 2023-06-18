from django.contrib import admin

from admin_web.models import Task, Telegram


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "title", "created_at")


@admin.register(Telegram)
class TelegramAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "telegram_id", "created_at")
