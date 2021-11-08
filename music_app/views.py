from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
# Create your views here.
from django.core.paginator import Paginator
from read_app.models import Nhac
#
def music(request):
    paginator = Paginator(Nhac.objects.all(),1)
    recommended_music = Nhac.objects.all()
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"page_obj":page_obj, "nhac": recommended_music}
    return render(request,"music-page.html",context)

# Create your views here.

# def music(request):
#     recommended_music = Nhac.objects.all()
#     context = {"nhac": recommended_music}
#     return render(request, "music-page.html", context)


# def music(request):
#     return render(request, 'music-page.html', {})
