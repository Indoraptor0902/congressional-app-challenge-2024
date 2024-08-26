from django.db import models

# Create your models here.


class UserInfo(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username


class Pregnancies(models.Model):
    userinfo = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    pregnancies = models.IntegerField()

    def __str__(self):
        return str(self.pregnancies)

class Glucose(models.Model):
    userinfo = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    glucose = models.IntegerField()

    def __str__(self):
        return str(self.glucose)

class BloodPressure(models.Model):
    userinfo = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    bloodpressure = models.IntegerField()

    def __str__(self):
        return str(self.bloodpressure)

class SkinThickness(models.Model):
    userinfo = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    skinthickness = models.IntegerField()

    def __str__(self):
        return str(self.skinthickness)

class Insulin(models.Model):
    userinfo = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    insulin = models.IntegerField()

    def __str__(self):
        return str(self.insulin)

class Height(models.Model):
    userinfo = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    height = models.IntegerField()

    def __str__(self):
        return str(self.height)

class Weight(models.Model):
    userinfo = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    weight = models.IntegerField()

    def __str__(self):
        return str(self.weight)

class DiabetesPedigreeFunction(models.Model):
    userinfo = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    diabetespedigreefunction = models.FloatField()

    def __str__(self):
        return str(self.diabetespedigreefunction)

class Age(models.Model):
    userinfo = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    age = models.IntegerField()

    def __str__(self):
        return str(self.age)