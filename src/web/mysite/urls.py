from django.urls import path, include

from mysite.views import indexView, RegisterView, TaskCreateView, TaskCompleteView, TaskBackView, TaskDeleteView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', indexView, name='index'),
    path('register/', RegisterView.as_view(), name='register'),
    path('create_task/', TaskCreateView.as_view(), name='create_task'),
    path('complete_task/<int:task_id>', TaskCompleteView.as_view(), name='complete_task'),
    path('back_task/<int:task_id>', TaskBackView.as_view(), name='back_task'),
    path('delete_task/<int:task_id>', TaskDeleteView.as_view(), name='delete_task'),
]
