# Generated by Django 4.1 on 2022-08-05 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0010_school_pedagogy_alter_advantage_phrase'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to='schools/banners'),
        ),
    ]
