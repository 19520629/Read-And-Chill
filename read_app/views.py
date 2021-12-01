from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import RegistrationForm, CommentForm
from django.http import HttpResponseRedirect
from .models import Sach, Nhac, Account, Comment, Favorite
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

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

@login_required(login_url='/login/')
def book_page(request):
    recommended_book = Sach.objects.all()
    context = {"titles": recommended_book}
    return render(request, 'book-page.html', context)

@login_required(login_url='/login/')
def introbook(request, slug):
    post = get_object_or_404(Sach, slug=slug)
    recommended_book = Sach.objects.all()
    comment_object = Comment.objects.filter(post=post)
    comment_form = CommentForm(request.POST)

    if request.method == 'POST':
        if 'comment' in request.POST:
            comment_form = CommentForm(request.POST or None)
            if comment_form.is_valid():
                body = request.POST.get('body')
                comment = Comment.objects.create(post=post, user=request.user, body=body)
                comment.save()
                return HttpResponseRedirect(request.path_info)
            else:
                comment_form= CommentForm()
        elif 'delete' in request.POST:
            comment = Comment.objects.get(id=request.POST['comment_id'])
            comment.delete()
            return HttpResponseRedirect(request.path_info)
        
    

    context = {"titles": recommended_book, "slug":slug,
               "comments": comment_object,"comment_form": comment_form}
    return render(request, 'intro-book.html', context)

@login_required(login_url='/login/')
def delete_comment(request):
    post = get_object_or_404(Sach, slug=slug)
    comment = Comment.objects.get(id=request.POST['comment_id'])
    comment.delete()
    return HttpResponseRedirect(request.path_info)


@login_required(login_url='/login/')
def readbook(request, slug, slug2):
    book = get_object_or_404(Sach, slug=slug2)
    book.book_luotxem += 0.5
    book.save()
    recommended_music = Nhac.objects.all()
    recommended_book = Sach.objects.all()


    context = {"titles": recommended_book, "slug":slug, "nhac": recommended_music}
    book.save()
    return render(request, 'read-book.html', context)



def search(request):
    dulieu=request.POST['search']
    recommended_book = Sach.objects.filter(book_tensach__icontains=dulieu)
    recommended_music = Nhac.objects.filter(song_tenbaihat=dulieu)
    context = {"titles": recommended_book, "nhac": recommended_music, "slug":dulieu}
    return render(request, 'search-page.html', context)


@login_required(login_url='/login/')
def search_book1(request):
    dulieu='VN'
    recommended_book = Sach.objects.filter(book_quocgia__icontains=dulieu)
    context = {"titles": recommended_book, "slug":dulieu}
    return render(request, 'search-page.html', context)


@login_required(login_url='/login/')
def search_book2(request):
    dulieu='nuocngoai'
    national=dulieu
    recommended_book = Sach.objects.filter(book_quocgia__icontains=national)
    context = {"titles": recommended_book,  "slug":dulieu}
    return render(request, 'search-page.html', context)

@login_required(login_url='/login/')
def search_music1(request):
    dulieu='VN'
    recommended_music = Nhac.objects.filter(song_quocgia__icontains=dulieu)
    context = {"nhac": recommended_music, "slug":dulieu}
    return render(request, 'search-page.html', context)


@login_required(login_url='/login/')
def search_music2(request):
    dulieu='nuocngoai'
    recommended_music = Nhac.objects.filter(song_quocgia__icontains=dulieu)
    context = {"nhac": recommended_music, "slug":dulieu}
    return render(request, 'search-page.html', context)
