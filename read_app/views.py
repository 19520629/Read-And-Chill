from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import RegistrationForm, CommentForm
from django.http import HttpResponseRedirect
from .models import Sach, Nhac, Account, Comment
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
    post = get_object_or_404(Sach, slug=slug)
    recommended_book = Sach.objects.all()
    comment_object = Comment.objects.filter(post=post)
    comment_form = CommentForm(request.POST)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            body = request.POST.get('body')
            comment = Comment.objects.create(post=post, user=request.user, body=body)
            comment.save()
            return HttpResponseRedirect(request.path_info)
        else:
            comment_form= CommentForm()


    context = {"titles": recommended_book, "slug":slug,
               "comments": comment_object,"comment_form": comment_form}
    return render(request, 'intro-book.html', context)


def readbook(request, slug, slug2):
    recommended_music = Nhac.objects.all()
    recommended_book = Sach.objects.all()
    context = {"titles": recommended_book, "slug":slug, "nhac": recommended_music}
    return render(request, 'read-book.html', context)


# def search(request):
#     recommended_book = Sach.objects.all()
#     context = {"titles": recommended_book, "slug": slug}
#     recommended_music = Nhac.objects.all()
#     context = {"titles": recommended_book, "slug": slug, "music":recommended_music}
#     return render(request, 'search-page.html', context)


def search(request):
    # search_term = ''
    # if 'search' in request.POST:
    #     search_term = request.POST['search']
    # book = Sach.objects.all()
    # return render(request, 'search-page.html', {'items': book, 'slug': search_term})
    dulieu=request.POST['search']
    recommended_book = Sach.objects.all()
    recommended_music = Nhac.objects.all()
    context = {"titles": recommended_book, "nhac": recommended_music, "slug":dulieu}
    return render(request, 'search-page.html', context)

# class AddComment(request):
#
#     model = Comment
#     form_class = CommentForm
#     template_name = 'intro-book.html'
#     # fields = '__all__'
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)
#
#     success_url = reverse_lazy('introbook')

