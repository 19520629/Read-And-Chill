from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/',auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('book/', views.book_page, name='book'),
    path('bookdetail/<slug:slug>', views.readbook, name = 'book_detail'),
    path('preview/<slug:slug>', views.previewbook, name = 'preview_book'),
]