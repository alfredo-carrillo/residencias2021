from django import forms
from django.db.models import fields
from django.forms import ModelForm
from business.models import Business, Contact
from django.contrib.auth.models import User
from django import forms

class BusinessForm(ModelForm):
    class Meta:
        model = Business
        # fields = ['name', 'first_name', 'last_name', 'rfc',]
        fields = '__all__'
        exclude = ['user', 'contact']

        def clean_rfc(self):
            rfc = self.cleaned_data.get('rfc')
            if Business.objects.filter(rfc=rfc).exists():
                raise forms.ValidationError("Este RFC ya existe")
            return rfc

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

        def clean_email(self):
            email = self.cleaned_data.get('email')
            if Business.objects.filter(email=email).exists():
                raise forms.ValidationError("Este email ya existe")
            return email
        
        def clean_phone1(self):
            phone1 = self.cleaned_data.get('phone1')
            if Business.objects.filter(phone1=phone1).exists():
                raise forms.ValidationError("Este teléfono ya existe")
            return phone1

        def clean_phone2(self):
            phone2 = self.cleaned_data.get('phone2')
            if Business.objects.filter(phone2=phone2).exists():
                raise forms.ValidationError("Este teléfono ya existe")
            return phone2

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        exclude = ['first_name', 'groups','last_name', 'is_staff', 'is_active', 'is_superuser', 'last_login', 'date_joined', 
        'user_permissions', 'password']