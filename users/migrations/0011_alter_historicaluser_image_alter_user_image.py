# Generated by Django 5.1.1 on 2024-09-10 23:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_historicaluser_last_login_ip_user_last_login_ip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaluser',
            name='image',
            field=models.TextField(blank=True, default='profile_picture/Isotipo.png', max_length=100, null=True, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp'])]),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='profile_picture/Isotipo.png', null=True, upload_to='profile_picture/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp'])]),
        ),
    ]