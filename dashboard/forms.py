from django.forms import ModelForm
from schools.models import *


class ProfileForm(ModelForm):

    class Meta:
        model = School
        fields = ('crest', 'thumbnail', 'banner', 'name', 'email', 'website', 'address',
                  'tel', 'cel', 'moto', 'year_founded', 'resumption')


class DetailForm(ModelForm):

    class Meta:
        model = School
        fields = ('history', 'description',
                  'ad_copy', 'mgt_quote')


class AcademiaForm(ModelForm):

    class Meta:
        model = School
        fields = (
            'availability', 'pedagogy', 'awards', 'diplomas',
            'courses', 'time_range', 'price_range', 'edu_levels')


class StuctureForm(ModelForm):

    class Meta:
        model = School
        fields = ('faculties', 'classes', 'labs', 'libs', 'canteens',
                  'staff', 'students', 'curriculums', 'success_rate')

# ---------------------------------------------------


class TeacherForm(ModelForm):

    class Meta:
        model = School
        fields = ('__all__')
        exclude = ('school',)


class ClassForm(ModelForm):

    class Meta:
        model = School
        fields = ('__all__')
        exclude = ('school',)
