# Generated by Django 5.0 on 2024-01-27 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trial_class_reservation', '0005_alter_content_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservationform',
            name='comment',
            field=models.TextField(null=True, verbose_name='自由記入欄'),
        ),
    ]
