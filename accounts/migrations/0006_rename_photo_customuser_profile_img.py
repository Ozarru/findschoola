# Generated by Django 4.0.3 on 2022-08-16 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_customuser_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='photo',
            new_name='profile_img',
        ),
    ]
