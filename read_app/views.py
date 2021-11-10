from django.shortcuts import render, HttpResponse
from .forms import RegistrationForm
from django.http import HttpResponseRedirect
from .models import Sach
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
    recommended_book=Sach.objects.all()
    context={"titles":recommended_book[0:10]}
    return render(request, 'index.html', context)


def book_page(request):
    recommended_book = Sach.objects.all()
    context = {"titles": recommended_book}
    return render(request, 'book-page.html', context)


def introbook(request, slug):
    recommended_book = Sach.objects.all()
    context = {"titles": recommended_book, "slug":slug}
    return render(request, 'intro-book.html', context)


def readbook(request, slug):
    recommended_book = Sach.objects.all()
    context = {"titles": recommended_book, "slug":slug}
    return render(request, 'read-book.html', context)