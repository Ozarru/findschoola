# Generated by Django 4.0.3 on 2022-08-16 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0033_rename_subperk_subscriptionperk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classroom',
            name='label',
        ),
        migrations.AddField(
            model_name='classroom',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
    ]
