# Generated by Django 5.1.1 on 2024-09-10 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multimedia', '0011_rename_multimediaclassification_historicalmultimedia_multimediaclassification_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalmultimedia',
            old_name='multimediaClassification',
            new_name='multimediaclassification',
        ),
        migrations.RenameField(
            model_name='multimedia',
            old_name='multimediaClassification',
            new_name='multimediaclassification',
        ),
    ]