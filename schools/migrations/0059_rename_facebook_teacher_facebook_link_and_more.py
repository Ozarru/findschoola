# Generated by Django 4.1 on 2022-10-04 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0058_rename_cursus_school_systems'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='facebook',
            new_name='facebook_link',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='instagram',
            new_name='instagram_link',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='linkedin',
            new_name='linkedin_link',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='twitter',
            new_name='twitter_link',
        ),
    ]
