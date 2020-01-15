from django.shortcuts import render, redirect
from predictions.models import Prediction
from .forms import PredictionForm

def prediction_index(request):
    predictions = Prediction.objects.all()
    return render(request, 'predictions/index.html', {'predictions': predictions})

def prediction_new(request):
    if request.method == "POST":
        form = PredictionForm(request.POST)
        if form.is_valid():
            prediction = form.save(commit=False)
            prediction.save()
            return redirect('/predictions/')
    else:
        form = PredictionForm()
        return render(request,'predictions/new.html', {'form': form})
