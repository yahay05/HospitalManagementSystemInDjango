from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_patient = models.BooleanField(default=True)

class Person(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=40)
    mobile = models.CharField(max_length=50)
    gender = models.ForeignKey("Gender",default='Other',on_delete=models.SET_DEFAULT)
    
    class Meta:
        abstract=True

class Doctor(Person):
    user = models.OneToOneField("User", on_delete=models.CASCADE)
    speciality = models.ForeignKey("Speciality",related_name='doctors',null=True,blank=True,on_delete=models.SET_NULL)
    
    def __str__(self):
        return f'{self.name} {self.surname}'

class Patient(Person):
    user = models.OneToOneField("User", on_delete=models.CASCADE)
    address = models.TextField(null=True,blank=True)
    
    def __str__(self):
        return f'{self.name} {self.surname}'

class Appointment(models.Model):
    doctor = models.ForeignKey("Doctor",on_delete=models.CASCADE)
    patient = models.ForeignKey("Patient",on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    
    def __str__(self):
        return self.date

class Speciality(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Gender(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

