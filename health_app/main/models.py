from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class HealthInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='health_info')
    age = models.PositiveIntegerField(blank=True, default=0)
    bmi = models.FloatField(blank=True, default=0)
    insulin = models.FloatField(blank=True, default=0)
    glucose = models.FloatField(blank=True, default=0)
    blood_pressure = models.FloatField(blank=True, default=0)

    def __str__(self):
        return f"{self.user.username}'s Health Information"


