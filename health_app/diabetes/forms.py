from django import forms

class DiabetesPredictionForm(forms.Form):
    pregnancies = forms.IntegerField(label="Number Of Pregnancies")
    glucose = forms.IntegerField(label="Glucose Level")
    bloodpressure = forms.IntegerField(label="Diastolic Blood Pressure")
    skinthickness = forms.IntegerField(label="Skin Thickness")
    insulin = forms.IntegerField(label="Insulin")
    bmi = forms.FloatField(label="BMI")
    diabetespedigreefunction = forms.FloatField(label="Diabetes Pedigree Function")
    age = forms.IntegerField(label="Age")