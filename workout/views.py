from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from workout.models import Workout, Exercise, ExerciseSet
from .forms import WorkoutForm

class WorkoutDetailView(DetailView):
    model = Workout

class WorkoutCreateView(CreateView):
    model = Workout
    form_class = WorkoutForm
    def form_valid(self,form):
        instance = form.save(commit=False)
        return super().form_valid(form)
    def get_success_url(self):
        return '/'
