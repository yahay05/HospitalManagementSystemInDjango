from django import forms
from .models import User, Gender
from django.contrib.auth.forms import UserCreationForm, UsernameField

class PatientForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email')
        field_classes = {'username':UsernameField,'email':forms.EmailField}
    
    name = forms.CharField(max_length=30)
    surname = forms.CharField(max_length=40)
    mobile = forms.CharField(max_length=50)
    gender = forms.ModelChoiceField(queryset=Gender.objects.all())
    address = forms.CharField(widget=forms.Textarea)