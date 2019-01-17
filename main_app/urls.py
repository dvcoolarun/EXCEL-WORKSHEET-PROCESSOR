from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from main_app import views

urlpatterns = [
    path('', views.file_upload, name='file_upload'),
    path('dashboard/', views.dashboard, name='dashboard')
]
