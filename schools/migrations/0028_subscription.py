# Generated by Django 4.0.3 on 2022-08-13 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0027_delete_subscription'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('tier', models.CharField(choices=[('free', 'Gratuit'), ('basic', 'Basique'), ('pro', 'Professionel')], default='free', max_length=50, null=True)),
                ('duration', models.CharField(choices=[('month', 'Mois'), ('trimester', 'Trimestre'), ('semester', 'Semestre'), ('year', 'Annuel')], default='month', max_length=50, null=True)),
                ('price', models.IntegerField(default='0')),
            ],
        ),
    ]
