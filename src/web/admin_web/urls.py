from django.urls import path

from admin_web.views import ApiGetTaskView, ApiTaskCreateView, ApiGetAllTasksView

urlpatterns = [
    path('get_all_tasks/<int:telegram_id>', ApiGetAllTasksView.as_view(), name='api_get_all_tasks'),
    path('get_task/<int:telegram_id>/<int:task_id>', ApiGetTaskView.as_view(), name='api_get_task'),
    path('create_task/<int:telegram_id>', ApiTaskCreateView.as_view(), name='api_create_task'),
]
