# Generated by Django 4.1 on 2022-09-30 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0057_school_professors'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='cursus',
            new_name='systems',
        ),
    ]