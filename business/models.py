from django.db import models
from django.contrib.auth.models import User
from employees.models import Contact
from encrypted_model_fields.fields import EncryptedCharField
# Create your models here.

class Business(models.Model):
    name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    rfc = models.CharField(max_length=13, unique=True)
    #contact = models.ForeignKey(Contact, on_delete=models.CASCADE, null=True)
    user = models.ManyToManyField(User, null=True)

    def __str__(self):
        return self.name

class CSD(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    #cer = models.FieldFile(upload_to= "")
    cer = models.FileField(upload_to ='csds')
    key = models.FileField(upload_to= 'csds')
    passphrase = EncryptedCharField(max_length=100)