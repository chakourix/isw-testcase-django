from django.db import models

class TeamMember(models.Model):
    name = models.CharField(max_length=48)
    email = models.CharField(max_length=48)
    phoneNumber = models.CharField(max_length=48)
    isAdmin = models.CharField(max_length=1)