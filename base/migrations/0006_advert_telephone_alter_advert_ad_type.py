# Generated by Django 4.1 on 2022-08-29 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_advert_ad_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='telephone',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='advert',
            name='ad_type',
            field=models.CharField(blank=True, choices=[('demand', 'Demande'), ('offer', 'Offre')], default='', max_length=50, null=True),
        ),
    ]
