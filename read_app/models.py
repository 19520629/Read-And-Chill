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
    book_tomtat=models.CharField(max_length=255)
    book_danhgia=models.FloatField(default=0)# Sua thanh float vi danh gia tính trung binh nen em sợ có số lẻ
    slug=models.SlugField(max_length=100)
    def __str__(self):
        return self.book_tensach

class CaSi(models.Model):
    song_casi_id=models.IntegerField(null=False)
    song_casi_ten=models.CharField(default='',max_length=255)
    def __str__(self):
        return self.song_casi_ten


class Nhac(models.Model):
    song_id=models.IntegerField(null=False)
    song_tenbaihat=models.CharField(max_length=255)
    song_anhbia=models.FileField()
    song_quocgia=models.CharField(max_length=100)
    song_danhgia=models.FloatField(default=0)
    song_file=models.FileField(upload_to='music')
    song_casi_id=models.ForeignKey(CaSi, on_delete=models.CASCADE)
    def __str__(self):
        return self.song_tenbaihat


class Favorite(models.Model):
    favlist_id=models.IntegerField(null=False)
    book_id=models.ForeignKey(Sach, on_delete=models.CASCADE)
    song_id=models.ForeignKey(Nhac, on_delete=models.CASCADE)


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
    hoten = models.CharField(max_length=255)
    gioitinh = models.CharField(max_length=1, choices=sex_choice, )
    user_avt = models.FileField()

    def __str__(self):
        return self.user.username