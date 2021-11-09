# Generated by Django 3.2.8 on 2021-11-01 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('read_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avt_id', models.IntegerField()),
                ('avt', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='nhac',
            name='song_anhbia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='read_app.anh'),
        ),
        migrations.AlterField(
            model_name='sach',
            name='book_anhbia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='read_app.anh'),
        ),
    ]