# Generated by Django 5.1.1 on 2024-09-10 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multimedia', '0010_rename_multimediaclassification_historicalmultimedia_multimediaclassification_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalmultimedia',
            old_name='multimediaclassification',
            new_name='multimediaClassification',
        ),
        migrations.RenameField(
            model_name='multimedia',
            old_name='multimediaclassification',
            new_name='multimediaClassification',
        ),
    ]
