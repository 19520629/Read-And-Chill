# Generated by Django 3.2.8 on 2021-11-29 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('read_app', '0028_alter_favorite_item_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favorite',
            old_name='item_name',
            new_name='is_Sach',
        ),
    ]