from django.db import models 
from django.contrib.auth.models import AbstractUser

class CustomUserModel(AbstractUser):
    def __str__(self):
        return self.username


class ProfileModel(models.Model):
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=[
        ('male', 'male'),
        ('female', 'female'),
    ])
    age = models.IntegerField()
    height = models.DecimalField(max_digits=4, decimal_places=2)
    weight = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name

class CaloryIntakeModel(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    item = models.CharField(max_length=100)
    calory = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(null=True)
    def __str__(self):
        return self.item