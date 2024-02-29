# Generated by Django 4.2 on 2024-01-24 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'Administrador'), ('editor', 'Editor'), ('reader', 'Lector')], default='reader', max_length=10),
        ),
    ]
