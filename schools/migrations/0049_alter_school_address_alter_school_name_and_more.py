# Generated by Django 4.1 on 2022-09-01 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0048_remove_school_is_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='address',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='school',
            name='tel',
            field=models.CharField(default='', max_length=255),
        ),
    ]