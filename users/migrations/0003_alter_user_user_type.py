# Generated by Django 5.0 on 2024-01-09 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('', '--- Select user type ---'), (0, '通塾生'), (1, '体験')], default=0, max_length=20),
        ),
    ]
