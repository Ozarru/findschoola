# Generated by Django 4.1 on 2022-09-30 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0055_rename_xp_teacher_years_of_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Structure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='schools/laboratories')),
                ('genre', models.CharField(choices=[('lab', 'Laboratoire'), ('lib', 'Bibliotheque'), ('can', 'Cantine'), ('gym', 'Espace de sport'), ('pool', 'Piscine')], default='', max_length=50)),
                ('label', models.CharField(default='image label', max_length=255)),
                ('maxseats', models.IntegerField(default='0')),
                ('info', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='laboratory',
            name='school',
        ),
        migrations.RemoveField(
            model_name='library',
            name='school',
        ),
        migrations.RemoveField(
            model_name='school',
            name='courses',
        ),
        migrations.AddField(
            model_name='school',
            name='cursus',
            field=models.IntegerField(blank=True, default='0', null=True),
        ),
        migrations.AddField(
            model_name='school',
            name='divisions',
            field=models.IntegerField(blank=True, default='0', null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='designation',
            field=models.CharField(choices=[('prof', 'Prof.'), ('doc', 'Doc.'), ('mr', 'M.'), ('mrs', 'Mme'), ('ms', 'Mlle')], default='', max_length=50),
        ),
        migrations.DeleteModel(
            name='Canteen',
        ),
        migrations.DeleteModel(
            name='Laboratory',
        ),
        migrations.DeleteModel(
            name='Library',
        ),
        migrations.AddField(
            model_name='structure',
            name='school',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='schools.school'),
        ),
    ]
