# Generated by Django 4.0.3 on 2022-08-13 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0026_alter_subscription_price'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Subscription',
        ),
    ]
