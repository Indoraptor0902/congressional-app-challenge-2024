from django.shortcuts import render
from .forms import DiabetesPredictionForm
from .predictor import DiabetesPredictor

# Create your views here.

def predict_diabetes(request):
    statement = ""
    if request.method == 'POST':
        form = DiabetesPredictionForm(request.POST)
        if form.is_valid():
            predictor = DiabetesPredictor()
            print((form.cleaned_data["weight"] * 703) / (form.cleaned_data["height"] ** 2))
            user_values = [
                form.cleaned_data["pregnancies"],
                form.cleaned_data["glucose"],
                form.cleaned_data["bloodpressure"],
                form.cleaned_data["skinthickness"],
                form.cleaned_data["insulin"],
                (form.cleaned_data["weight"] * 703) / (form.cleaned_data["height"] ** 2),
                form.cleaned_data["diabetespedigreefunction"],
                form.cleaned_data["age"],
            ]
            result = predictor.has_diabetes(user_values)
            statement = "You are at risk of diabetes." if result else "You are not at risk of diabetes."
            return render(request, 'index.html', {'form': form, 'statement': statement})
    else:
        form = DiabetesPredictionForm()

    return render(request, 'index.html', {'form': form, 'statement': statement})