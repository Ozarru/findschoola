# Generated by Django 4.1 on 2022-09-27 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0050_rename_report_schblog_remove_school_awards_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Schblog',
            new_name='Blog',
        ),
    ]
