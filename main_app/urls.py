from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from main_app import views

urlpatterns = [
    path('upload/', views.simple_upload, name='simple_upload')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
