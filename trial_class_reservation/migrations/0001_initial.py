# Generated by Django 5.0 on 2024-01-04 01:23

import django.db.models.deletion
import modelcluster.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contents', '0006_alter_tag_options_alter_textcategory_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='日付')),
                ('capacity', models.IntegerField(verbose_name='定員(予約の上限数)')),
                ('available', models.BooleanField(default=True, verbose_name='Is Active')),
            ],
        ),
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_tiem', models.TimeField(verbose_name='開始時刻')),
                ('end_time', models.TimeField(verbose_name='終了時刻')),
            ],
        ),
        migrations.CreateModel(
            name='ReservationForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child_name1', models.CharField(max_length=255, verbose_name='お子様の氏名(漢字)')),
                ('child_name2', models.CharField(max_length=255, verbose_name='お子様の氏名(ふりがな)')),
                ('parent_name1', models.CharField(max_length=255, verbose_name='保護者の氏名(漢字)')),
                ('parent_name2', models.CharField(max_length=255, verbose_name='保護者の氏名(ふりがな)')),
                ('email', models.EmailField(max_length=254, verbose_name='メールアドレス')),
                ('phone_number', models.CharField(max_length=255, verbose_name='電話番号')),
                ('comment', models.TextField(verbose_name='自由記入欄')),
                ('content', modelcluster.fields.ParentalManyToManyField(blank=True, to='contents.textcategory', verbose_name='コンテンツのカテゴリ選択')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trial_class_reservation.schedule', verbose_name='希望日時')),
            ],
        ),
        migrations.AddField(
            model_name='schedule',
            name='timeslot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trial_class_reservation.timeslot', verbose_name='時間割を選択'),
        ),
    ]