from django.db import models
from django.utils import timezone  

  
   
class Patient(models.Model):
    first_name = models.CharField(max_length=25, null=True)
    middle_name = models.CharField(max_length=25, null=True)
    last_name = models.CharField(max_length=25, null=True)
    email = models.EmailField()
    address = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    gender_choices = (
      ('female', 'Female'),
      ('male', 'Male'),
      ('other', 'other'),
    )
    gender = models.CharField(max_length=8, null=True, choices=gender_choices)
    age = models.PositiveSmallIntegerField(null=True)
    password = models.IntegerField(null=True)
    weight = models.PositiveSmallIntegerField(default=0)
    # profile_image = models.ImageField()
    next_of_kin = models.CharField(max_length=30,null=True)
    phone_number_Next_of_kin = models.IntegerField(null=True)

