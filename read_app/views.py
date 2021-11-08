from django.shortcuts import render, HttpResponse
from .forms import RegistrationForm
from django.http import HttpResponseRedirect
from .models import Sach
# Create your views here.
def home(request):
    recommended_book=Sach.objects.all()
    context={"titles":recommended_book[0:10]}
    return render(request, 'index.html', context)


def register(request):
    form=RegistrationForm()
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'dangki.html', {'form':form})


def book_page(request):
    return render(request, 'book-page.html', {})

def readbook(request):
    return render(request, 'read-book.html', {})

def previewbook(request):
    return render(request, 'intro-book.html', {})
