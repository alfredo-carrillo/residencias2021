from django.db import models
from django.contrib.auth.models import User
from django.db.models.enums import Choices
# Create your models here.

#modelo empleado    
class Employee(models.Model):
    antiquity = models.CharField(max_length=20, null=True) #Antiguedad
    curp = models.CharField(max_length=18)
    date_of_entry = models.DateField(max_length=12, null=True)
    num_employee = models.CharField(max_length=6) #numero de empleado
    nss = models.CharField(max_length= 11)
    position = models.CharField(max_length=50) #puesto
    salary_base = models.CharField(max_length=8, null=True)
    salary_diary = models.CharField(max_length=8, null=True)
    unionized = models.CharField(max_length=2, null=True) #sindicalizado
    rfc = models.CharField(max_length=13)
    user =models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

#Modelo contacto
class Contact(models.Model):
    email = models.EmailField()
    phone1 = models.CharField(max_length=10, null=True)
    phone2 = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=60)
    # employee = models.ForeignKey(Employee, on_delete=models.CASCADE)