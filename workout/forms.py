from django import forms
from django.forms import ModelForm

from .models import Workout

class DateInput(forms.DateInput):
    input_type = 'date'

class WorkoutForm(ModelForm):
    class Meta:
        model = Workout
        fields = ['date', 'time_of_day', 'title', 'notes']
        widgets = { 'date': DateInput()}
