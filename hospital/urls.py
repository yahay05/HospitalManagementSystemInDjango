from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView

app_name = 'hospital'

urlpatterns = [
        path('',HomePageView.as_view(),name='home-page'),
        path('about/',AboutPageView.as_view(),name='about-page'),
        path('contact/',ContactPageView.as_view(),name='contact-page'),

]
