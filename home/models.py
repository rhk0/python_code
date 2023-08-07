from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone_number = PhoneNumberField(blank=True)
    desc = models.CharField(max_length=155, default=None, null=True, blank=True)
    date = models.DateField(null=True,blank=True,default=None)
    field1 = models.IntegerField(null=True,blank=True,default=None)
    field2 = models.IntegerField(null=True,blank=True,default=None)
    result = models.IntegerField(null=True,blank=True,default=None)



    
