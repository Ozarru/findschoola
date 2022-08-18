from django.forms import ModelForm
from schools.models import *


class ProfileForm(ModelForm):

    class Meta:
        model = School
        fields = ('crest', 'thumbnail', 'banner', 'name', 'email', 'website', 'address',
                  'tel', 'cel', 'moto', 'year_founded', 'resumption')
        exclude = ("user", "subscription", "is_featured")


class DetailForm(ModelForm):

    class Meta:
        model = School
        fields = ('history', 'description',
                  'ad_copy', 'faculties', 'mgt_quote')


class AcademiaForm(ModelForm):

    class Meta:
        model = School
        fields = (
            'availability', 'pedagogy', 'awards', 'diplomas',
            'courses', 'time_range', 'price_range', 'edu_levels',
            'staff', 'students', 'inscription', 'curriculums', 'success_rate')


class StuctureForm(ModelForm):

    class Meta:
        model = School
        fields = ('classes', 'labs', 'libs', 'canteens', 'faculties')
