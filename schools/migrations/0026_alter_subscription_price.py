# Generated by Django 4.0.3 on 2022-08-13 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0025_remove_subscription_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='price',
            field=models.IntegerField(default='0'),
        ),
    ]