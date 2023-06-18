from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + [
    path('admin/', admin.site.urls, name='admin_panel'),
    path('', include('mysite.urls')),
    path('api/v1/', include('admin_web.urls')),
]
