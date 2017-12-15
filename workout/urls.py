from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from workout.views import WorkoutDetailView, WorkoutCreateView

urlpatterns = [
    url(r'^workout/(?P<pk>\d+)/$', WorkoutDetailView.as_view(), name='workout_detail_view'),
    url(r'^workout-create/$', WorkoutCreateView.as_view(), name='workout_create_view'),
]
