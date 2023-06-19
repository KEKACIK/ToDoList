from django.http import JsonResponse
from django.views import View

from admin_web.models import Telegram, Task


class ApiTaskCreateView(View):
    def get(self, request, telegram_id):
        telegram = Telegram.objects.get(telegram_id=int(telegram_id))
        if not telegram or not telegram.user:
            return JsonResponse({'result': 'id dont register'})
        user = telegram.user
        if not request.GET.get('title'):
            return JsonResponse({'result': 'title error'})
        title = request.GET.get('title')
        if not request.GET.get('description'):
            return JsonResponse({'result': 'description error'})
        description = request.GET.get('description')
        try:
            Task(user=user, title=title, description=description).save()
            return JsonResponse({'result': 'success'})
        except:
            return JsonResponse({'result': 'data error'})
