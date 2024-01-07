# Generated by Django 5.0 on 2024-01-07 22:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0006_alter_tag_options_alter_textcategory_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='textpage',
            name='categories',
        ),
        migrations.AddField(
            model_name='textpage',
            name='categories',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='contents.textcategory', verbose_name='コンテンツのカテゴリ選択'),
        ),
    ]
