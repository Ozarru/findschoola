from django.db import models
from django.urls import reverse
from django.utils import timezone
from accounts.models import CustomUser
# from multiselectfield import MultiSelectField


class EduLevel(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


infrastructure = (
    ('lab', 'Laboratoire'),
    ('lib', 'Bibliotheque'),
    ('can', 'Cantine'),
    ('gym', 'Espace de sport'),
    ('pool', 'Piscine'),
)

designations = (
    ('prof', 'Prof.'),
    ('doc', 'Doc.'),
    ('mr', 'M.'),
    ('mrs', "Mme"),
    ('ms', "Mlle"),
)
tiers = (
    ('free', 'Gratuit'),
    ('basic', "Basique"),
    ('pro', "Professionel"),
)

durations = (
    ('undefined', 'Indéfini'),
    ('month', 'Mois'),
    ('trimester', "Trimestre"),
    ('semester', "Semestre"),
    ('year', "Année"),
)

LEVEL_CHOICES = (
    ('creche', 'Creche'),
    ('jardin', 'Jardin'),
    ('primaire', 'Primaire'),
    ('college', 'College'),
    ('lycee', 'Lycee'),
    ('universite', 'Universite'),
    ('centre-Academique', 'Centre-Academique'),
    ('centre-Professionnel', 'Centre-Professionnel'),
)


class Plan(models.Model):
    name = models.CharField(max_length=128)
    price = models.IntegerField(default='0')
    tier = models.CharField(
        max_length=50, null=True, default='free', choices=tiers)
    duration = models.CharField(
        max_length=50, null=True, default='undefined', choices=durations)

    def __str__(self):
        return self.name


class Subscription(models.Model):
    subscriber = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=False)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.subscriber.username


class School(models.Model):
    manager = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False, default='',)
    email = models.EmailField(blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, default='',)
    tel = models.CharField(max_length=255, default='',)
    cel = models.CharField(max_length=255, default='', blank=True, null=True)
    moto = models.CharField(max_length=255, blank=True, null=True)
    year_founded = models.CharField(max_length=4, blank=True, null=True)
    mgt_quote = models.TextField(blank=True, null=True)
    history = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    ad_copy = models.TextField(blank=True, null=True)
    resumption = models.CharField(
        max_length=180, default='', blank=True, null=True)

    # academia
    availability = models.TextField(blank=True, null=True)
    time_range = models.CharField(
        max_length=255, blank=True, null=True)
    price_range = models.CharField(
        max_length=255, blank=True, null=True)
    levels = models.ManyToManyField(EduLevel, blank=True)
    success_rate = models.IntegerField(default='0', blank=True, null=True)
    professors = models.IntegerField(default='0', blank=True, null=True)
    divisions = models.IntegerField(default='0', blank=True, null=True)
    systems = models.IntegerField(default='0', blank=True, null=True)

    # profile
    thumbnail = models.ImageField(
        upload_to='schools/thumbnails', blank=True, null=True)
    banner = models.ImageField(
        upload_to='schools/banners', blank=True, null=True)
    crest = models.ImageField(
        upload_to='schools/crests', blank=True, null=True)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('school', kwargs={'pk': self.pk})


class Photo(models.Model):
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, default=None)
    image = models.ImageField(
        upload_to='schools/photos', blank=True, null=True)


class Stat(models.Model):
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, default=None)
    year = models.CharField(max_length=4, default='year')
    pass_rate = models.IntegerField(default='0')
    fail_rate = models.IntegerField(default='0')


class Teacher(models.Model):
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, default=None)
    image = models.ImageField(
        upload_to='schools/teachers', blank=True, null=True)
    fullname = models.CharField(max_length=255)
    designation = models.CharField(
        max_length=50, default='', choices=designations)
    subjects = models.CharField(max_length=255)
    years_of_experience = models.IntegerField(default='0')
    qualifications = models.CharField(max_length=255, blank=True, null=True)
    tel = models.CharField(
        max_length=255, blank=True, null=True)
    facebook = models.CharField(
        max_length=255, blank=True, null=True)
    twitter = models.CharField(
        max_length=255, blank=True, null=True)
    instagram = models.CharField(
        max_length=255, blank=True, null=True)
    linkedin = models.CharField(
        max_length=255, blank=True, null=True)

    def __str__(self):
        return self.fullname


class Advantage(models.Model):
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, default=None)
    phrase = models.CharField(max_length=255, default='avantage',)


class Classroom(models.Model):
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, default=None)
    image = models.ImageField(
        upload_to='schools/classrooms', blank=True, null=True)
    name = models.CharField(max_length=255, default='')
    fee = models.IntegerField(default='0', blank=True, null=True)
    size = models.IntegerField(default='0', blank=True, null=True)
    maxseats = models.IntegerField(default='0', blank=True, null=True)
    info = models.TextField(blank=True, null=True)


class Structure(models.Model):
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, default=None)
    image = models.ImageField(
        upload_to='schools/laboratories', blank=True, null=True)
    genre = models.CharField(
        max_length=50, default='', choices=infrastructure)
    label = models.CharField(max_length=255, default='image label')
    info = models.TextField(blank=True, null=True)
    maxseats = models.IntegerField(default='0')
    info = models.TextField(blank=True, null=True)


class Article(models.Model):
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, default=None)
    image = models.ImageField(
        upload_to='schools/reports', blank=True, null=True)
    title = models.CharField(max_length=255, default='News Title')
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, default='News')
    date_posted = models.DateTimeField(auto_now=True)
