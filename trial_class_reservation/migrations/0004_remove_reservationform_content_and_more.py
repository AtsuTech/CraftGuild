# Generated by Django 5.0 on 2024-01-06 08:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trial_class_reservation', '0003_content_alter_schedule_available'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservationform',
            name='content',
        ),
        migrations.AddField(
            model_name='reservationform',
            name='content',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='trial_class_reservation.content', verbose_name='コンテンツのカテゴリ選択'),
        ),
    ]
