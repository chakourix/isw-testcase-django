from django.db import models
from django.core.validators import validate_email

class TeamMember(models.Model):
    name = models.CharField(max_length=48)
    email = models.EmailField(unique=True,validators=[validate_email])
    phoneNumber = models.IntegerField(max_length=20)
    isAdmin = models.IntegerField(max_length=1)