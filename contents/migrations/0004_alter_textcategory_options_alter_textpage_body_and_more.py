# Generated by Django 5.0 on 2023-12-30 04:28

import modelcluster.contrib.taggit
import modelcluster.fields
import wagtailmarkdown.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0003_textcategory_tag_alter_textpage_body_and_more'),
        ('taggit', '0005_auto_20220424_2025'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='textcategory',
            options={'verbose_name': 'カテゴリ', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterField(
            model_name='textpage',
            name='body',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True, verbose_name='テキストの説明'),
        ),
        migrations.AlterField(
            model_name='textpage',
            name='categories',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='contents.textcategory', verbose_name='カテゴリ'),
        ),
        migrations.AlterField(
            model_name='textpage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='contents.TextPageTag', to='taggit.Tag', verbose_name='タグ'),
        ),
    ]