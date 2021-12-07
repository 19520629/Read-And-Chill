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
    #dfdfdfd
    path('login/',auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('book/', views.book_page, name='book'),
    path('book/<slug:slug>', views.introbook, name = 'introbook'),
    path('book/<slug:slug>/<slug:slug2>', views.readbook, name = 'readbook'),
    path('logout/', views.logout_view, name='logout'),
    path('search/', views.search, name='search'),
    path('search1/', views.search_book1, name='search1'),
    path('search2/', views.search_book2, name='search2'),
    path('search3/', views.search_music1, name='search3'),
    path('search4/', views.search_music2, name='search4'),
]
