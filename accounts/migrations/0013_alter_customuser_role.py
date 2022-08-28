# Generated by Django 4.1 on 2022-08-28 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_customuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(blank=True, choices=[('utilisateur', 'Utilisateur générique (Parent/Eleve)'), ('gestionaire', "Gestionaire d'école")], max_length=50, null=True),
        ),
    ]
