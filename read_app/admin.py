from django.contrib import admin
from .models import  Sach, Nhac, CaSi, TacGia, TheLoai, Favorite, Account, Comment
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class TheLoaiAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
class Sach_Admin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
class AccountInline(admin.StackedInline):
    model=Account
    can_delete = False
    verbose_name_plural = 'Accounts.'
class CustomizedUserAdmin(UserAdmin):
    inlines = (AccountInline,)
admin.site.register(Nhac)
admin.site.register(CaSi)
admin.site.register(TacGia)
admin.site.register(TheLoai)
admin.site.register(Favorite)
admin.site.register(Sach)
admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)
admin.site.register(Comment)