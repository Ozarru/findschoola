# Generated by Django 4.1 on 2022-08-19 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_remove_customuser_profile_img_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='anon.jpg', null=True, upload_to='users'),
        ),
    ]
