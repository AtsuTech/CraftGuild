# Generated by Django 5.0 on 2024-01-07 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trial_class_reservation', '0004_remove_reservationform_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='イメージ画像'),
        ),
    ]
