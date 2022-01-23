from rest_framework import serializers
from app.models import Exercise, Workout
from django.contrib.auth.models import User


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'


class WorkoutSerializer(serializers.ModelSerializer):
    exercises = ExerciseSerializer(read_only=True, many=True)

    class Meta:
        model = Workout
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    workouts = WorkoutSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = '__all__'
