import pdb
from django import forms
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic import CreateView, TemplateView
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from business.models import Business
from .forms import BusinessForm, ContactForm, UserForm
from django.urls import reverse_lazy
# Create your views here.

class BusinessCreateView(CreateView):
    template_name = 'business/business_form.html'
    model = Business
    form_class = BusinessForm
    success_url = reverse_lazy('register-sucess')

    def get_context_data(self, *args, **kwargs):
        context_data = super(BusinessCreateView, self).get_context_data(*args, **kwargs)
        if self.request.method == 'GET':
            context_data['UserForm'] = UserForm
        return context_data
    
    # def post(self, request, *args, **kwargs):
    #     form = self.get_form()
    #     if form.is_valid():
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)
    def get_user_form(self):
        if self.request.method == 'POST':
            return UserForm(self.request.POST)

    def form_valid(self, form):
        try:
            self.UserForm = self.get_user_form()

            if self.UserForm.is_valid():
                self.object = form.save(commit=False)
                
                name = form.data.get('name')      
                first_name = form.data.get('first_name')
                last_name = form.data.get('last_name')
                rfc = form.data.get('rfc')
                email = form.data.get('email')
                username = form.data.get('username')
                #phone2 = form.data.get('phone2')
                #address = form.data.get('address')
                #crear objeto user
                user_obj = User.objects.create(email=email, username=username)
                business_obj = Business.objects.create(name=name, first_name=first_name, last_name=last_name, rfc=rfc)
                business_obj.user.add(user_obj)
                business_obj.save()
                return super(BusinessCreateView, self).form_valid(form)
            else:
                return super(BusinessCreateView, self).form_invalid(form)
        except Exception as e:
            print(str(e))



    def send_activation_email(self, user):
        """
        Send the activation email. The activation key is the username,
        signed using TimestampSigner.
        """
        activation_key = self.get_activation_key(user)
        context = self.get_email_context(activation_key)
        context["user"] = user
        subject = render_to_string(
            template_name=self.email_subject_template,
            context=context,
            request=self.request,
        )
        # Force subject to a single line to avoid header-injection
        # issues.
        subject = "".join(subject.splitlines())
        message = render_to_string(
            template_name=self.email_body_template,
            context=context,
            request=self.request,
        )
        send_mail (
            subject, 
            '',
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            html_message=message,
            fail_silently=False,
        )

class Registration_sucess(TemplateView):
    template_name = 'business/registro.html'


class Home(TemplateView):
    template_name = 'home.html'
