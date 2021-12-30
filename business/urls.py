from django.http import request
from .views import BusinessCreateView, Registration_sucess, Home
from django.urls import path

urlpatterns = [
    path('register/', BusinessCreateView.as_view(), name="business_form"),
    path('register/sucess',Registration_sucess.as_view(), name="register-sucess" ),
    path('home', Home.as_view(), name='home')
]