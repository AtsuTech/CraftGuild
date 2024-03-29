# Generated by Django 5.0 on 2024-01-27 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0011_contentstags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentsdetailpage',
            name='explanation',
            field=models.TextField(blank=True, null=True, verbose_name='コンテンツの説明'),
        ),
        migrations.AlterField(
            model_name='contentsdetailpage',
            name='note',
            field=models.TextField(blank=True, null=True, verbose_name='備考'),
        ),
    ]
