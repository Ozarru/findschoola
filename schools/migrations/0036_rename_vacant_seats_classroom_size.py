# Generated by Django 4.1 on 2022-08-16 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0035_alter_classroom_fee_alter_classroom_maxseats_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classroom',
            old_name='vacant_seats',
            new_name='size',
        ),
    ]
