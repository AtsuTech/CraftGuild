# Generated by Django 5.0 on 2023-12-28 11:05

import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0001_initial'),
        ('taggit', '0005_auto_20220424_2025'),
        ('wagtailcore', '0089_log_entry_data_json_null_to_object'),
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentsdetailpage',
            name='contents_name',
            field=models.CharField(max_length=100, verbose_name='コンテンツのタイトル'),
        ),
        migrations.AlterField(
            model_name='contentsdetailpage',
            name='cover_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='カバー写真'),
        ),
        migrations.AlterField(
            model_name='contentsdetailpage',
            name='explanation',
            field=wagtail.fields.RichTextField(blank=True, null=True, verbose_name='コンテンツの説明'),
        ),
        migrations.CreateModel(
            name='TextPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('text_name', models.CharField(max_length=100, verbose_name='コンテンツのタイトル')),
                ('body', wagtail.fields.RichTextField(blank=True, null=True, verbose_name='コンテンツの説明')),
                ('cover_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='カバー写真')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='TextPageTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='contents.textpage')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_items', to='taggit.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='textpage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='contents.TextPageTag', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
