from django.urls import path

from admin_web.views import ApiGetTaskView, ApiCreateView

urlpatterns = [
    path('get_all_tasks/<int:telegram_id>', ApiGetTaskView.as_view(), name='api_get_all_tasks'),
    path('create_task/<int:telegram_id>', ApiCreateView.as_view(), name='api_create_task'),
]
