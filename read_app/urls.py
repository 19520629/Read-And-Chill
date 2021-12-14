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
    path('update/', views.updateuser, name='updateuser'),
    path('login/',auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('book/', views.book_page, name='book'),
    path('book/<slug:slug>', views.introbook, name = 'introbook'),
    path('book/<slug:slug>/<slug:slug2>', views.readbook, name = 'readbook'),
    path('logout/', views.logout_view, name='logout'),
    path('search/', views.search, name='search'),
    path('search1/', views.search_book1, name='search1'),
    path('search2/', views.search_book2, name='search2'),   
    path('filter-book-qt1/', views.filter_book_quoctich1, name='filter-book-qt1'),
    path('filter-book-qt2/', views.filter_book_quoctich2, name='filter-book-qt2'),
    path('filter-book-tg1/', views.filter_book_tacgia1, name='filter-book-tg1'),
    path('filter-book-tg2/', views.filter_book_tacgia2, name='filter-book-tg2'),
    path('filter-book-tg3/', views.filter_book_tacgia3, name='filter-book-tg3'),
    path('filter-book-tl1/', views.filter_book_theloai1, name='filter-book-tl1'),
    path('filter-book-tl2/', views.filter_book_theloai2, name='filter-book-tl2'),
    path('filter-book-tl3/', views.filter_book_theloai3, name='filter-book-tl3'),
    path('filter-music-qt1/', views.filter_music_quoctich1, name='filter-music-qt1'),
    path('filter-music-qt2/', views.filter_music_quoctich2, name='filter-music-qt2'),
    path('filter-music-tb1/', views.filter_music_trinhbay1, name='filter-music-tb1'),
    path('filter-music-tb2/', views.filter_music_trinhbay2, name='filter-music-tb2'),
    path('filter-music-tb3/', views.filter_music_trinhbay3, name='filter-music-tb3'),
]
