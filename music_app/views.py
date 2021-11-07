from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
# Create your views here.

def music(request):
    return render(request, 'music-page.html', {})
