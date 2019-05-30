from django.db import models

# Create your models here.
class User(models.Model):
    uname = models.CharField(max_length=255)
    upass = models.CharField(max_length=60)
    email= models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    gender = models.CharField(max_length=6)
    birth= models.CharField(max_length=20)
    acc_type = models.CharField(max_length=15)

    def __str__(self):
        return self.uname + " " + self.upass

