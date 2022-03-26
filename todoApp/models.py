from django.db import models
class Userinf(models.Model):
    username = models.CharField(max_length=12)
    group    = models.CharField(max_length=20)
    password = models.CharField(max_length=12)