from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class TrainingSession(models.Model):
    SESSION_TYPES = (
        ('run', 'Run'),
        ('gym', 'Gym'),
        ('workout', 'Workout'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    date = models.DateField()
    notes = models.TextField(blank=True, null=True)
    session_type = models.CharField(max_length=10, choices=SESSION_TYPES)

    def __str__(self):
        return f"{self.user.name}'s {self.title} on {self.date}"


class Run(models.Model):
    session = models.OneToOneField(TrainingSession, on_delete=models.CASCADE, primary_key=True)
    distance_meters = models.PositiveIntegerField()
    duration_minutes = models.PositiveIntegerField()

    @property
    def average_speed(self):
        return self.distance_meters / 1000 / (self.duration_minutes / 60)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class TrainingExercise(models.Model):
    session = models.ForeignKey(TrainingSession, on_delete=models.CASCADE)
    exercise_name = models.CharField(max_length=150)
    sets = models.PositiveSmallIntegerField()
    reps = models.PositiveSmallIntegerField()
    weight = models.FloatField(blank=True, null=True)
    additional_weight = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.exercise_name} in {self.session.title}"
