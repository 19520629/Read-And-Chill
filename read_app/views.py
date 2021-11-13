from django.shortcuts import render, HttpResponse, redirect
from .forms import RegistrationForm
from django.http import HttpResponseRedirect
from .models import Sach, Nhac, Account
from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.

def register(request):
    form=RegistrationForm()
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'dangki.html', {'form':form})


def home(request):
    recommended_book = Sach.objects.all()
    recommended_music = Nhac.objects.all()
    context={"titles":recommended_book[0:10], "nhac":recommended_music[0:5]}
    return render(request, 'index.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


def book_page(request):
    recommended_book = Sach.objects.all()
    context = {"titles": recommended_book}
    return render(request, 'book-page.html', context)


def introbook(request, slug):
    recommended_book = Sach.objects.all()
    context = {"titles": recommended_book, "slug":slug}
    return render(request, 'intro-book.html', context)


def readbook(request, slug, slug2):
    recommended_book = Sach.objects.all()
    context = {"titles": recommended_book, "slug":slug}
    return render(request, 'read-book.html', context)


def search(request, slug):
    recommended_book = Sach.objects.all()
    context = {"titles": recommended_book, "slug": slug}
    recommended_music = Nhac.objects.all()
    context = {"titles": recommended_book, "slug": slug, "music":recommended_music}
    return render(request, 'search-page.html', context)