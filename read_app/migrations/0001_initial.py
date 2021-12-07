# Generated by Django 3.2.8 on 2021-12-01 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CaSi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_casi_ten', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TacGia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_tacgia_id', models.IntegerField()),
                ('book_tacgia', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TheLoai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_theloai_id', models.IntegerField()),
                ('book_theloai', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Sach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_tensach', models.CharField(max_length=255)),
                ('book_quocgia', models.CharField(max_length=100)),
                ('book_noidung', models.FileField(upload_to='pdf')),
                ('book_anhbia', models.ImageField(upload_to='cover_book')),
                ('book_tomtat', models.TextField()),
                ('book_danhgia', models.FloatField(default=0)),
                ('book_luotxem', models.FloatField(default=0)),
                ('slug', models.SlugField(max_length=100)),
                ('book_tacgia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='read_app.tacgia')),
                ('book_theloai_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='read_app.theloai')),
            ],
        ),
        migrations.CreateModel(
            name='Nhac',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_tenbaihat', models.CharField(max_length=255)),
                ('song_anhbia', models.FileField(upload_to='')),
                ('book_luotnghe', models.FloatField(default=0)),
                ('song_quocgia', models.CharField(max_length=100)),
                ('song_danhgia', models.FloatField(default=0)),
                ('song_file', models.FileField(upload_to='music')),
                ('song_casi_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='read_app.casi')),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_Sach', models.BooleanField()),
                ('favlist_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='read_app.sach')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='read_app.sach')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hoten', models.CharField(max_length=255, null=True)),
                ('gioitinh', models.CharField(choices=[('F', 'Nu'), ('M', 'NAM'), ('A', 'Khac')], max_length=1, null=True)),
                ('user_avt', models.ImageField(default='static/assets/img/default-avatar.png', upload_to='avt')),
                ('tuoi', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
