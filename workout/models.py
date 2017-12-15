from django.db import models

EXERCISE_TYPE = [('standard', 'standard'), ('cardio', 'cardio'), ('power', 'power'), ('growth', 'growth'),
                  ('cutting', 'cutting'), ('movement', 'movement'), ('speed', 'speed'), ('functional', 'functional')]

INTENSITY_RATING = [(i,i) for i in range(1,11)]

class Workout(models.Model):
    time = models.DateTimeField()
    title = models.CharField(max_length=40)
    notes = models.TextField(null=True,blank=True)

class Exercise(models.Model):
    workout = models.ForeignKey(Workout,on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    exercise_type = models.CharField(max_length=40,choices=EXERCISE_TYPE)
    intensity = models.IntegerField(choices=INTENSITY_RATING)
    notes = models.TextField(null=True,blank=True)

class ExerciseSet(models.Model):
    exercise = models.ForeignKey(Exercise,on_delete=models.CASCADE)
    weight_lbs = models.FloatField()
    rep_amount = models.IntegerField()
    rep_completed = models.IntegerField()
    notes = models.TextField(null=True,blank=True)
