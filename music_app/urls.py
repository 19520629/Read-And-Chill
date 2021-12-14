from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('music/', views.music, name='music'),
    path('music1/', views.music1, name='music1'),
    path('music2/', views.music2, name='music2'),
    path('music3/', views.music3, name='music3'),
    path('music4/', views.music4, name='music4'),
    path('music5/', views.music5, name='music5'),
]