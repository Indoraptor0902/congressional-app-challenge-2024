from django import forms

class DiabetesPredictionForm(forms.Form):
    pregnancies = forms.IntegerField(label="Number Of Pregnancies")
    glucose = forms.IntegerField(label="Glucose Level")
    bloodpressure = forms.IntegerField(label="Diastolic Blood Pressure")
    skinthickness = forms.IntegerField(label="Skin Thickness")
    insulin = forms.IntegerField(label="Insulin")
    height = forms.FloatField(label="Height (Inches)")
    weight = forms.FloatField(label="Weight (Pounds)")
    diabetespedigreefunction = forms.FloatField(label="Diabetes Pedigree Function")
    age = forms.IntegerField(label="Age")