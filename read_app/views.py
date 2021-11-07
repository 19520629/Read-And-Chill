from django.shortcuts import render, HttpResponse
from .forms import RegistrationForm
from django.http import HttpResponseRedirect
from .models import Sach
# Create your views here.
def home(request):
    recommended_book=Sach.objects.all()
    context={"titles":recommended_book}
    return render(request, 'index.html', context)


def register(request):
    form=RegistrationForm()
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'dangki.html', {'form':form})


def gallery(request):
    img = Sach.objects.filter(file_type='book_anhbia')
    return render(request,'gallery.html',{"img":img, 'media_url':settings.MEDIA_URL})


