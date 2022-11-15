from django.shortcuts import render
from django.shortcuts import render,redirect,reverse
from django.views import generic
from .forms import PatientForm
from .models import Patient,User



class HomePageView(generic.TemplateView):
    template_name = 'hospital/home_page.html'

class AboutPageView(generic.TemplateView):
    template_name = 'hospital/about_page.html'

class ContactPageView(generic.TemplateView):
    template_name = 'hospital/contact_page.html'

class PatientSignupView(generic.CreateView):
    template_name = 'registration/patient_signup.html'
    form_class = PatientForm
    
    def get_success_url(self):
        return reverse('login')
    
    def form_valid(self,form):
        form.save(commit=True)
        cleaned_form = form.cleaned_data
        print(cleaned_form)
        patient = Patient(user = User.objects.get(username=cleaned_form['username']),name = cleaned_form['name'],surname=cleaned_form['surname'],gender=cleaned_form['gender'],mobile=cleaned_form['mobile'],address=cleaned_form['address'])
        patient.save()
        return super(PatientSignupView,self).form_valid(form)


