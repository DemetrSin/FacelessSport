from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, ListView
from .models import TrainingSession, Run, TrainingExercise
from .forms import TrainingSessionForm, RunForm, TrainingExerciseForm


class TrainingSessionCreateView(View):
    def get(self, request):
        form = TrainingSessionForm()
        return render(request, 'training_session_form.html', {'form': form})

    def post(self, request):
        form = TrainingSessionForm(request.POST)
        if form.is_valid():
            training_session = form.save(commit=False)
            training_session.user = request.user
            training_session.save()
            if training_session.session_type == 'run':
                return redirect('run_create', pk=training_session.pk)
            return redirect('exercise_create', pk=training_session.pk)
        return render(request, 'training_session_form.html', {'form': form})


class RunCreateView(View):
    def get(self, request, pk):
        form = RunForm()
        return render(request, 'run_form.html', {'form': form, 'session_id': pk})

    def post(self, request, pk):
        form = RunForm(request.POST)
        if form.is_valid():
            run = form.save(commit=False)
            run.session = TrainingSession.objects.get(pk=pk)
            run.save()
            return redirect('session_detail', pk=pk)
        return render(request, 'run_form.html', {'form': form, 'session_id': pk})


class TrainingExerciseCreateView(View):
    def get(self, request, pk):
        form = TrainingExerciseForm()
        return render(request, 'training_exercise_form.html', {'form': form, 'session_id': pk})

    def post(self, request, pk):
        form = TrainingExerciseForm(request.POST)
        if form.is_valid():
            training_exercise = form.save(commit=False)
            training_exercise.session = TrainingSession.objects.get(pk=pk)
            training_exercise.save()
            return redirect('session_detail', pk=pk)
        return render(request, 'training_exercise_form.html', {'form': form, 'session_id': pk})


class TrainingSessionDetailView(DetailView):
    model = TrainingSession
    template_name = 'session_detail.html'
    context_object_name = 'session'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        session = self.get_object()
        if session.session_type == 'run':
            context['run'] = Run.objects.get(session=session)
        else:
            context['exercises'] = TrainingExercise.objects.filter(session=session)
        return context


class UserTrainingListView(ListView):
    model = TrainingSession
    template_name = 'training_session_list.html'
    context_object_name = 'training_sessions'

    def get_queryset(self):
        return TrainingSession.objects.filter(user=self.request.user)
