# Generated by Django 5.0 on 2024-01-27 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0010_contentsdetailpage_note_and_more'),
        ('taggit', '0005_auto_20220424_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentsTags',
            fields=[
            ],
            options={
                'verbose_name': 'コンテンツのタグ',
                'verbose_name_plural': 'コンテンツのタグ管理',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('taggit.tag',),
        ),
    ]
