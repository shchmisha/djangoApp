from django.db import models
from django.contrib.auth.models import User


class Workout(models.Model):
    name = models.CharField(max_length=10)
    date = models.DateField(blank=True, null=True)
    user = models.ForeignKey(
        User, related_name='workouts', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Exercise(models.Model):
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=50)
    type = models.CharField(max_length=2)
    workout = models.ForeignKey(
        Workout, related_name='exercises', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
