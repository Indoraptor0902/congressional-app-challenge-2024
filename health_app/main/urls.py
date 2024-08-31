from django.urls import path
from . import views

urlpatterns = [
    path('update-health-info/', views.update_health_info, name='update_health_info'),
    path('health-info-success/', views.health_info_success, name='health_info_success'),
]