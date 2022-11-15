from django.contrib import admin
from .models import Doctor, Patient, Appointment, Gender, Speciality, User

admin.site.register(User)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Speciality)
admin.site.register(Gender)
