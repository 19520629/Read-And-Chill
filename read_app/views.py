from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import RegistrationForm, CommentForm, UserUpdateForm, AccountUpdateForm
from django.http import HttpResponseRedirect
from .models import Sach, Nhac, Account, Comment, Favorite
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
import re
import sys
from django.contrib.auth.models import User


# Create your views here.
#function
patterns = {
    '[àáảãạăắằẵặẳâầấậẫẩ]': 'a',
    '[đ]': 'd',
    '[èéẻẽẹêềếểễệ]': 'e',
    '[ìíỉĩị]': 'i',
    '[òóỏõọôồốổỗộơờớởỡợ]': 'o',
    '[ùúủũụưừứửữự]': 'u',
    '[ỳýỷỹỵ]': 'y'
}

def convert(text):
    """
    Convert from 'Tieng Viet co dau' thanh 'Tieng Viet khong dau'
    text: input string to be converted
    Return: string converted
    """
    output = text
    for regex, replace in patterns.items():
        output = re.sub(regex, replace, output)
        # deal with upper case
        output = re.sub(regex.upper(), replace.upper(), output)
    return output
#
def register(request):
    form=RegistrationForm()
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'dangki.html', {'form':form})

def updateuser(request):
    user = request.user
    account = Account.objects.get(user=user)
    form=AccountUpdateForm()
    if user.is_anonymous:
        #permissiondenied
        return redirect('/')
    else:
        if request.method=='POST':
            form=AccountUpdateForm(request.POST or None,request.FILES, instance=account)
            if form.is_valid():
                instance = form.save(commit=False)
                print(request.POST)
                instance.save()
                print(instance.user_avt)
                return redirect('book')
    return render(request, 'updateuser.html', {'form':form, 'user': user})


love_book=Favorite.objects.filter(user_id=User.username)

def home(request):
    
    recommended_book = Sach.objects.all()
    recommended_music = Nhac.objects.all()


    current_user=request.user
    fav=[]
    fav_list=Favorite.objects.filter(user_id=current_user)
    for i in fav_list:
        fav.append(Sach.objects.get(id=i.book_id))
    context={"titles":recommended_book[0:10], "nhac":recommended_music[0:5], "fav":fav}
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
    dulieu=slug
    post = get_object_or_404(Sach, slug=slug)
    recommended_book = Sach.objects.filter(slug=slug)
    fav_list=Sach.objects.filter(slug=slug)
    comment_object = Comment.objects.filter(post=post)
    comment_form = CommentForm(request.POST)
    book =  get_object_or_404(Sach, slug=slug)
    current_user = request.user
    path=  str(current_user.username) + str(book.id)
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


        elif 'like' in request.POST:            
            check_exists=Favorite.objects.filter(user_book=path).exists()
            if check_exists==False:
                b = Favorite(user_book=path, user_id=current_user.username, book_id=book.id)
                b.save()
                book.book_danhgia+=1
                book.save()
            else:
                book.book_danhgia-=1
                book.save()
                b=Favorite.objects.get(user_book=path)
                b.delete()
            return HttpResponseRedirect(request.path_info)
    
    fav=[]
    fav_list=Favorite.objects.filter(user_id=current_user)
    for i in fav_list:
        fav.append(Sach.objects.get(id=i.book_id))
    
    fav_list = Favorite.objects.filter(book_id=book.id)
    fav_list=fav_list.filter(book_id=book.id)
    context = {"titles": recommended_book, "slug":slug, "comments": comment_object, "comment_form": comment_form, "fav_check":fav_list, "fav":fav}
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
    book.book_luotxem += 1
    book.save()
    recommended_music = Nhac.objects.all()
    recommended_book = Sach.objects.all()


    current_user=request.user
    fav=[]
    fav_list=Favorite.objects.filter(user_id=current_user)
    for i in fav_list:
        fav.append(Sach.objects.get(id=i.book_id))

    context = {"titles": recommended_book, "slug":slug, "nhac": recommended_music,"fav":fav}
    book.save()

    
    return render(request, 'read-book.html', context)



def search(request):
    dulieu=request.POST['search']
    recommended_book1=[]
    recommended_music1=[]
    dulieu=(convert(dulieu)).lower().replace(" ", "")
    #book
    recommended_book = Sach.objects.all()
    for item in recommended_book:
        tensach=convert(item.book_tensach+item.book_tacgia.book_tacgia).lower().replace(" ", "")
        if dulieu in tensach:
            recommended_book1.append(item)
            
    #music
    recommended_music = Nhac.objects.all()    
    for item in recommended_music:
        tennhac=convert(item.song_tenbaihat + item.song_casi_id.song_casi_ten).lower().replace(" ", "")
        if dulieu in tennhac:
            recommended_music1.append(item)

    current_user=request.user
    fav=[]
    fav_list=Favorite.objects.filter(user_id=current_user)
    for i in fav_list:
        fav.append(Sach.objects.get(id=i.book_id))


    context = {"titles": recommended_book1, "nhac": recommended_music1, "slug":dulieu, "fav":fav}
    return render(request, 'search-page.html', context)


@login_required(login_url='/login/')
def search_book1(request):
    dulieu='VN'
    recommended_book = Sach.objects.filter(book_quocgia__icontains=dulieu)


    current_user=request.user
    fav=[]
    fav_list=Favorite.objects.filter(user_id=current_user)
    for i in fav_list:
        fav.append(Sach.objects.get(id=i.book_id))
        

    context = {"titles": recommended_book, "slug":dulieu, "fav":fav}
    return render(request, 'search-page.html', context)


@login_required(login_url='/login/')
def search_book2(request):
    dulieu='nuocngoai'
    
    recommended_book = Sach.objects.filter(book_quocgia=dulieu)
    current_user=request.user
    fav=[]
    fav_list=Favorite.objects.filter(user_id=current_user)
    for i in fav_list:
        fav.append(Sach.objects.get(id=i.book_id))

    context = {"titles": recommended_book, "slug":dulieu, "fav":fav}
    return render(request, 'search-page.html', context)

@login_required(login_url='/login/')
def search_music1(request):
    dulieu='VN'
    recommended_music = Nhac.objects.filter(song_quocgia__icontains=dulieu)
    current_user=request.user
    fav=[]
    fav_list=Favorite.objects.filter(user_id=current_user)
    for i in fav_list:
        fav.append(Sach.objects.get(id=i.book_id))

    context = {"titles": recommended_music, "slug":dulieu, "fav":fav}
    return render(request, 'search-page.html', context)


@login_required(login_url='/login/')
def search_music2(request):
    dulieu='nuocngoai'
    recommended_music = Nhac.objects.filter(song_quocgia__icontains=dulieu)
    current_user=request.user
    fav=[]
    fav_list=Favorite.objects.filter(user_id=current_user)
    for i in fav_list:
        fav.append(Sach.objects.get(id=i.book_id))

    context = {"titles": recommended_music, "slug":dulieu, "fav":fav}
    return render(request, 'search-page.html', context)

@login_required(login_url='/login/')
def search_book1(request):
    dulieu='VN'
    recommended_book = Sach.objects.filter(book_quocgia__icontains=dulieu)
    current_user=request.user
    fav=[]
    fav_list=Favorite.objects.filter(user_id=current_user)
    for i in fav_list:
        fav.append(Sach.objects.get(id=i.book_id))

    context = {"titles": recommended_book, "slug":dulieu, "fav":fav}
    return render(request, 'search-page.html', context)

@login_required(login_url='/login/')
def filter_book_quoctich1(request):
    dulieu='VN'
    recommended_book = Sach.objects.filter(book_quocgia__icontains=dulieu)
    current_user=request.user
    fav=[]
    fav_list=Favorite.objects.filter(user_id=current_user)
    for i in fav_list:
        fav.append(Sach.objects.get(id=i.book_id))

    context = {"titles": recommended_book, "slug":dulieu, "fav":fav}
    return render(request, 'search-page.html', context)

@login_required(login_url='/login/')
def filter_book_quoctich2(request):
    dulieu='nuocngoai'
    recommended_book = Sach.objects.filter(book_quocgia__icontains=dulieu)
    context = {"titles": recommended_book, "slug":dulieu}
    return render(request, 'book-filter.html', context)



@login_required(login_url='/login/')
def filter_book_tacgia1(request):
    dulieu='Nguyễn Nhật Ánh'
    recommended_book = Sach.objects.filter(book_tacgia=dulieu)
    current_user=request.user
    fav=[]
    fav_list=Favorite.objects.filter(user_id=current_user)
    for i in fav_list:
        fav.append(Sach.objects.get(id=i.book_id))

    context = {"titles": recommended_book, "slug":dulieu, "fav":fav}
    return render(request, 'search-page.html', context)

@login_required(login_url='/login/')
def filter_book_tacgia2(request):
    dulieu='J.K. Rowling'
    recommended_book = Sach.objects.filter(book_tacgia__icontains=dulieu)
    current_user=request.user
    fav=[]
    fav_list=Favorite.objects.filter(user_id=current_user)
    for i in fav_list:
        fav.append(Sach.objects.get(id=i.book_id))

    context = {"titles": recommended_book, "slug":dulieu, "fav":fav}
    return render(request, 'search-page.html', context)
@login_required(login_url='/login/')
def filter_book_tacgia3(request):
    dulieu='Paulo Coelho'
    recommended_book = Sach.objects.filter(book_tacgia__icontains=dulieu)
    current_user=request.user
    fav=[]
    fav_list=Favorite.objects.filter(user_id=current_user)
    for i in fav_list:
        fav.append(Sach.objects.get(id=i.book_id))

    context = {"titles": recommended_book, "slug":dulieu, "fav":fav}
    return render(request, 'search-page.html', context)

# @login_required(login_url='/login/')
# def profile(request):
#     if request.method == 'POST':
#         u_form = UserUpdateForm(request.POST, instance=request.user)
#         p_form = AccountUpdateForm(request.POST, request.FILES,instance=request.user.profile)
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = AccountUpdateForm(instance=request.user.profile)
#         messages.success(request, f'Cập nhật thông tin thành công!')
#         return redirect('profile')
#
#     context = {
#         'u_form': u_form,
#         'p_form': p_form
#
#     }
#     return render(request, 'modal-user.html', context)


# objects.get(id=request.user.id)


@login_required(login_url='/login/')
def edit_profile(request):
    if request.method == 'POST':
        # profile = Account.objects.get(user_ID=request.user.account.id)
        user = User.objects.get(user_ID=request.user.account.id)
        # profile.hoten = request.POST['hoten']
        # profile.tuoi = request.POST['tuoi']
        user.account.hoten = request.POST['hoten']
        user.save()
        user.account.hoten.save()
        user.account.save()


    return redirect('modal-user.html',{'profile':profile})






