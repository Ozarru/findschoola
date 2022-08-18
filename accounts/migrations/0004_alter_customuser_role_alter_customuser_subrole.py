# Generated by Django 4.0.3 on 2022-08-11 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_customuser_photo_alter_customuser_subrole'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('utilisateur', 'Utilisateur générique'), ('gestionaire', "Gestionaire d'école")], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='subrole',
            field=models.CharField(choices=[('admin', 'School Admin'), ('editor', 'School Editor')], max_length=50, null=True),
        ),
    ]
