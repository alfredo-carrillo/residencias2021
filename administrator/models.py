from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name_department = (
        (0, 'Desarrollo de software'),
        (1, 'Soporte'),
        (2, 'Cobranza'),
        (3, 'Seguridad de la información'),
        (4, 'Infraestructura'),
)
    