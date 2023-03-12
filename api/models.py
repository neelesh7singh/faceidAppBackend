from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class User(models.Model):
    number = models.CharField(max_length=10, unique=True, validators=[MinLengthValidator(10, 'Phone number should be 10 digits long')])
    otp = models.CharField(max_length=6, validators=[MinLengthValidator(6, 'OTP should be 6 digits long')])
    created = models.DateField(auto_now_add=True, blank=True)


    