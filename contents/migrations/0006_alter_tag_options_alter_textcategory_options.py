# Generated by Django 5.0 on 2024-01-04 01:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0005_alter_textpage_body_alter_textpage_cover_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'タグ', 'verbose_name_plural': 'テキストのタグ管理'},
        ),
        migrations.AlterModelOptions(
            name='textcategory',
            options={'verbose_name': 'カテゴリ', 'verbose_name_plural': 'テキストのカテゴリ管理'},
        ),
    ]
