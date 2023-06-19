from django.http import JsonResponse
from django.views import View

from admin_web.models import Telegram, Task


class ApiGetAllTasksView(View):
    def get(self, request, telegram_id):
        telegram = Telegram.objects.get(telegram_id=int(telegram_id))
        if not telegram or not telegram.user:
            return JsonResponse({'result': 'id dont register'})
        user = telegram.user
        tasks = [{'id': task.id, 'title': task.title, 'description': task.description, 'close': task.close,
                  'created_at': task.created_at} for task in Task.objects.filter(user=user).all()]
        return JsonResponse({'result': 'success', 'items': tasks})


class ApiGetTaskView(View):
    def get(self, request, telegram_id, task_id):
        telegram = Telegram.objects.get(telegram_id=int(telegram_id))
        if not telegram or not telegram.user:
            return JsonResponse({'result': 'id dont register'})
        task = Task.objects.filter(user=telegram.user, id=task_id).get()
        if not task:
            return JsonResponse({'result': 'task not found'})
        return JsonResponse({'result': 'success',
                             'item': {'id': task.id, 'title': task.title, 'description': task.description,
                                      'close': task.close, 'created_at': task.created_at.strftime("%d-%m-%y %H:%M")}})
