# Generated by Django 5.0.6 on 2024-07-15 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multimedia', '0004_alter_multimedia_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='multimedia',
            old_name='name',
            new_name='title',
        ),
    ]
