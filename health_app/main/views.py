from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def update_health_info(request):
    user, created = User.objects.get_or_create(username='testuser')
    health_info, created = HealthInformation.objects.get_or_create(user=user)

    if request.method == "POST":
        health_info.age = request.POST.get('age')
        health_info.bmi = request.POST.get('bmi')
        health_info.insulin = request.POST.get('insulin')
        health_info.glucose = request.POST.get('glucose')
        health_info.blood_pressure = request.POST.get('blood_pressure')

        health_info.save()

        return redirect('health_info_success')

    return render(request, 'update_health_info.html', {
        'health_info': health_info
    })

def health_info_success(request):
    return render(request, 'health_info_success.html')