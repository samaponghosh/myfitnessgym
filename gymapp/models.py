from django.db import models
# from django.contrib.auth.models import User
# # Create your models here.

# class userData(models.Model):
#     username = models.CharField(max_length=60)
#     password = models.CharField(max_length=10)
#     last_name = models.CharField(max_length=10)
#     first_name = models.CharField(max_length=10)
    
class Enquiry(models.Model):
    name = models.CharField(max_length=60)
    contact = models.CharField(max_length=10)
    emailid = models.CharField(max_length=60)
    age = models.CharField(max_length=40)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.name
