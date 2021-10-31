from django.db import models

# Create your models here.
class TacGia(models.Model):
    book_tacgia_id=models.IntegerField(null=False)
    book_tacgia=models.CharField(default='',max_length=255)


class TheLoai(models.Model):
    book_theloai_id=models.IntegerField(null=False)
    book_theloai=models.CharField(max_length=255)


class Sach(models.Model):
    book_tensach= models.CharField(max_length=255)
    book_theloai_id =models.ForeignKey(TheLoai, on_delete=models.CASCADE, null=False)
    book_quocgia=models.CharField(max_length=100)
    book_tacgia=models.ForeignKey(TacGia, on_delete=models.CASCADE)
    book_noidung=models.CharField(max_length=255)
    book_anhbia=models.FileField()
    book_tomtat=models.CharField(max_length=255)
    book_danhgia=models.FloatField(default=0)# Sua thanh float vi danh gia tính trung binh nen em sợ có số lẻ


class CaSi(models.Model):
    song_casi_id=models.IntegerField(null=False)
    song_casi_ten=models.CharField(default='',max_length=255)


class Nhac(models.Model):
    song_id=models.IntegerField(null=False)
    song_tenbaihat=models.CharField(max_length=255)
    song_anhbia=models.FileField()
    song_quocgia=models.CharField(max_length=100)
    song_danhgia=models.FloatField(default=0)
    song_file=models.FileField()
    song_casi_id=models.ForeignKey(CaSi, on_delete=models.CASCADE)


class Favorite(models.Model):
    favlist_id=models.IntegerField(null=False)
    book_id=models.ForeignKey(Sach, on_delete=models.CASCADE)
    song_id=models.ForeignKey(Nhac, on_delete=models.CASCADE)


class User(models.Model):
    sex_choice=(
        ('F', 'Nu'),
        ('M', 'NAM'),
        ('A', 'Khac')
    )
    user_id=models.IntegerField(null=False)
    hoten=models.CharField(max_length=255)
    gioitinh=models.CharField(max_length=1, choices=sex_choice,)