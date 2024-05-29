from django.urls import path
from .views import (
    TrainingSessionCreateView,
    RunCreateView,
    TrainingExerciseCreateView,
    TrainingSessionDetailView,
    UserTrainingListView,
)

urlpatterns = [
    path('training-session/new/', TrainingSessionCreateView.as_view(), name='training_session_create'),
    path('training-session/<int:pk>/', TrainingSessionDetailView.as_view(), name='session_detail'),
    path('run/new/<int:pk>/', RunCreateView.as_view(), name='run_create'),
    path('exercise/new/<int:pk>/', TrainingExerciseCreateView.as_view(), name='exercise_create'),
    path('training-sessions/', UserTrainingListView.as_view(), name='training_session_list'),
]
