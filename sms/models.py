from django.db import models

# Create your models here.
class Sms(models.Model):
    sms = models.CharField(max_length=10000,default="Null")
    label = models.CharField(max_length=100,default="Not Predicted")
    
    def __str__(self):
        return self.sms
    