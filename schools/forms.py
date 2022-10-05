from django.forms import ModelForm
from django import forms
from schools.models import *


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ('__all__')
        exclude = ('manager',)

    levels = forms.ModelMultipleChoiceField(
        queryset=EduLevel.objects.all(), widget=forms.CheckboxSelectMultiple
    )


class AdvantageForm(ModelForm):
    class Meta:
        model = Advantage
        fields = ('__all__')
        exclude = ('school',)


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ('__all__')
        exclude = ('school',)


class ClassroomForm(ModelForm):
    class Meta:
        model = Classroom
        fields = ('__all__')
        exclude = ('school',)


class StructureForm(ModelForm):
    class Meta:
        model = Structure
        fields = ('__all__')
        exclude = ('school',)


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ('__all__')
        exclude = ('school', 'date_posted',)
