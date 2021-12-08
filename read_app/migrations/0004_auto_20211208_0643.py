# Generated by Django 3.2.9 on 2021-12-07 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('read_app', '0003_auto_20211207_1500'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteListSong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='account',
            name='gioitinh',
            field=models.CharField(choices=[('F', 'Nu'), ('M', 'Nam'), ('A', 'Khac')], max_length=1, null=True),
        ),
        migrations.CreateModel(
            name='FavoriteItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_book', models.CharField(default='', max_length=50)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='read_app.sach')),
                ('favorite_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='read_app.favoritelistsong')),
            ],
        ),
    ]
