from django.urls import path
from . import views

urlpatterns = [
    path('predictor', views.predict_diabetes)
]