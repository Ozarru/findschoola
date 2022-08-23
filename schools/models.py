from django.db import models
from django.urls import reverse
from django.utils import timezone
from accounts.models import CustomUser


class EduLevel(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


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


class Subscription(models.Model):
    name = models.CharField(max_length=128)
    tier = models.CharField(max_length=50, null=True,
                            default='free', choices=tiers)
    duration = models.CharField(
        max_length=50, null=True, default='undefined', choices=durations)
    price = models.IntegerField(default='0')

    def __str__(self):
        return self.name


class SubscriptionPerk(models.Model):
    subscription = models.ForeignKey(
        Subscription, on_delete=models.CASCADE)
    phrase = models.CharField(max_length=255, default='', null=False)

    def __str__(self):
        return self.subscription.price


class School(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    subscription = models.ForeignKey(
        Subscription, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    tel = models.CharField(max_length=255, default='', blank=True, null=True)
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
    pedagogy = models.TextField(blank=True, null=True)
    awards = models.CharField(
        max_length=255, blank=True, null=True)
    diplomas = models.CharField(
        max_length=255, blank=True, null=True)
    courses = models.CharField(
        max_length=255, blank=True, null=True)
    time_range = models.CharField(
        max_length=255, blank=True, null=True)
    price_range = models.CharField(
        max_length=255, blank=True, null=True)
    edu_levels = models.ManyToManyField(EduLevel, blank=True)
    staff = models.IntegerField(default='0', blank=True, null=True)
    students = models.IntegerField(default='0', blank=True, null=True)
    inscription = models.IntegerField(default='0', blank=True, null=True)
    curriculums = models.IntegerField(default='0', blank=True, null=True)
    success_rate = models.IntegerField(default='0', blank=True, null=True)

    # structures
    classes = models.IntegerField(default='0', blank=True, null=True)
    labs = models.IntegerField(default='0', blank=True, null=True)
    libs = models.IntegerField(default='0', blank=True, null=True)
    canteens = models.IntegerField(default='0', blank=True, null=True)
    faculties = models.IntegerField(default='0', blank=True, null=True)

    # profile
    is_featured = models.BooleanField(default=False)
    thumbnail = models.ImageField(
        upload_to='schools/thumbnails', blank=True, null=True)
    banner = models.ImageField(
        upload_to='schools/banners', blank=True, null=True)
    crest = models.ImageField(
        upload_to='schools/crests', blank=True, null=True)
    date_added = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super(School, self).save(*args, **kwargs)

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
    xp = models.IntegerField(default='0')
    fullname = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    subjects = models.CharField(max_length=255)
    qualifications = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(
        upload_to='schools/teachers', blank=True, null=True)
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
    # vacant_seats = models.IntegerField(default='0', blank=True, null=True)
    maxseats = models.IntegerField(default='0', blank=True, null=True)
    info = models.TextField(blank=True, null=True)


class Laboratory(models.Model):
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, default=None)
    image = models.ImageField(
        upload_to='schools/laboratories', blank=True, null=True)
    label = models.CharField(max_length=255, default='image label')
    info = models.TextField(blank=True, null=True)
    maxseats = models.IntegerField(default='0')


class Library(models.Model):
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, default=None)
    image = models.ImageField(
        upload_to='schools/libraries', blank=True, null=True)
    label = models.CharField(max_length=255, default='image label')
    info = models.TextField(blank=True, null=True)
    maxseats = models.IntegerField(default='0')


class Canteen(models.Model):
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, default=None)
    image = models.ImageField(
        upload_to='schools/canteens', blank=True, null=True)
    label = models.CharField(max_length=255, default='image label')
    info = models.TextField(blank=True, null=True)
    maxseats = models.IntegerField(default='0')


class Report(models.Model):
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, default=None)
    image = models.ImageField(
        upload_to='schools/reports', blank=True, null=True)
    title = models.CharField(max_length=255, default='News Title')
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, default='News')
    date_posted = models.DateTimeField(auto_now=True)
