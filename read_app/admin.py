from django.contrib import admin
from .models import Anh, Sach, Nhac, CaSi, TacGia, TheLoai, User, Favorite
# Register your models here.


class TheLoaiAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
class Sach_Admin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Anh)
admin.site.register(Nhac)
admin.site.register(CaSi)
admin.site.register(User)
admin.site.register(TacGia)
admin.site.register(TheLoai)
admin.site.register(Favorite)
admin.site.register(Sach)
