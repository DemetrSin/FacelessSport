from django import forms
from .models import TrainingSession, Run, TrainingExercise


class TrainingSessionForm(forms.ModelForm):
    class Meta:
        model = TrainingSession
        fields = ['title', 'date', 'notes', 'session_type']


class RunForm(forms.ModelForm):
    class Meta:
        model = Run
        fields = ['distance_meters', 'duration_minutes']


class TrainingExerciseForm(forms.ModelForm):
    class Meta:
        model = TrainingExercise
        fields = ['exercise_name', 'sets', 'reps', 'weight', 'additional_weight']
