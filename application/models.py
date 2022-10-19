from django.db import models
from traitlets import default

class UserData(models.Model):
    userid = models.BigAutoField(primary_key=True)
    useremail = models.EmailField(max_lenght = 30)
    username = models.CharField(max_lenght = 20, unique = True)
    userpass = models.CharField(max_lenght = 20, unique = True)
    uservrify = models.BooleanField(default = False)