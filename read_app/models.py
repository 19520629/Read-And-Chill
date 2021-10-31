from django.db import models

# Create your models here.
class Sach(models.Model):
    book_tensach= models.CharField(max_length=255)
    book_theloai-id =models.IntegerField()
    book_quocgia=models.CharField(max_length=100)
    book_tacgia=models.CharField(max_length=255)
    book_noidung=models.CharField(max_length=255)
    book_anhbia=