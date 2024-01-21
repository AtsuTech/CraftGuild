# Generated by Django 5.0 on 2024-01-15 10:30

import django.db.models.deletion
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0089_log_entry_data_json_null_to_object'),
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrialFlow',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('page_title', models.CharField(max_length=255, verbose_name='ページのタイトル')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='TrialFlowBlock',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('flow_title', models.CharField(max_length=255, verbose_name='体験の流れのタイトルのタイトル(例:体験授業60分)')),
                ('sub_title', wagtail.fields.RichTextField(blank=True, null=True, verbose_name='サブタイトル(例:STEP1)')),
                ('sub_title_color', models.CharField(choices=[('#BDE3FF', 'スカイブルー'), ('#FCD19C', 'オレンジ'), ('#FCC7C2', 'ピンク'), ('#99FF99', 'グリーン'), ('#C299FF', 'パープル'), ('#FFFF99', 'イエロー'), ('#FFFFFF', 'ホワイト'), ('#CCCCCC', 'グレー')], max_length=255, verbose_name='サブタイトルの背景カラー')),
                ('description', models.TextField(blank=True, verbose_name='体験の流れの詳細文')),
                ('order_check', models.BooleanField(default=True, verbose_name='最後のブロックかどうかの確認')),
                ('cover_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='カバー画像')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]