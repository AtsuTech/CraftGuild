# Generated by Django 5.0 on 2024-01-14 11:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_form', '0002_contactcategory_alter_contactform_contact_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='contact_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='contact_form.contactcategory', verbose_name='お問い合わせ内容選択'),
        ),
    ]