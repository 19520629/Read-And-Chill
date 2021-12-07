from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class TacGia(models.Model):
    book_tacgia_id=models.IntegerField(null=False)
    book_tacgia=models.CharField(default='',max_length=255)
    def __str__(self):
        return self.book_tacgia


class TheLoai(models.Model):
    book_theloai_id=models.IntegerField(null=False)
    book_theloai=models.CharField(max_length=255)
    slug=models.SlugField(max_length=50)
    def __str__(self):
        return self.book_theloai


class Sach(models.Model):
    book_tensach= models.CharField(max_length=255)
    book_theloai_id =models.ForeignKey(TheLoai, on_delete=models.CASCADE, null=False)
    book_quocgia=models.CharField(max_length=100)
    book_tacgia=models.ForeignKey(TacGia, on_delete=models.CASCADE)
    book_noidung=models.FileField(upload_to='pdf')
    book_anhbia=models.ImageField(upload_to='cover_book')
    book_tomtat=models.TextField()
    book_danhgia=models.FloatField(default=0)# Sua thanh float vi danh gia tính trung binh nen em sợ có số lẻ
    book_luotxem=models.FloatField(default=0)
    slug=models.SlugField(max_length=100)
    def __str__(self):
        return self.book_tensach

class CaSi(models.Model):

    song_casi_ten=models.CharField(default='',max_length=255)
    def __str__(self):
        return self.song_casi_ten


class Nhac(models.Model):
    song_tenbaihat=models.CharField(max_length=255)
    song_anhbia=models.FileField()
    book_luotnghe = models.FloatField(default=0)
    song_quocgia=models.CharField(max_length=100)
    song_danhgia=models.FloatField(default=0)
    song_file=models.FileField(upload_to='music')
    song_casi_id=models.ForeignKey(CaSi, on_delete=models.CASCADE)
    def __str__(self):
        return self.song_tenbaihat


class Favorite(models.Model):
    user_book=models.CharField(max_length=50, default='')
    user_id=models.CharField(max_length=50, default='')
    book_id=models.CharField(max_length=50, default='')

# class User(models.Model):
#     sex_choice=(
#         ('F', 'Nu'),
#         ('M', 'NAM'),
#         ('A', 'Khac')
#     )
#     user_id=models.IntegerField(null=False)
#     hoten=models.CharField(max_length=255)
#     gioitinh=models.CharField(max_length=1, choices=sex_choice,)
#     user_avt=models.FileField()
#     def __str__(self):
#         return self.hoten


class Account(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    sex_choice = (
        ('F', 'Nu'),
        ('M', 'NAM'),
        ('A', 'Khac')
    )
    hoten = models.CharField(max_length=255, null=True)
    gioitinh = models.CharField(max_length=1, choices=sex_choice, null=True)
    user_avt = models.ImageField(upload_to='avt', default='static/assets/img/default-avatar.png')
    tuoi=models.IntegerField(default=0)
    def __str__(self):
        return self.user.username


class Comment(models.Model):
    post = models.ForeignKey(Sach, related_name="comments" ,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.book_tensach, self.user.username)



