from django.db import models

# Create your models here.
class Mail(models.Model):
    mail = models.CharField(max_length=10000)
    label = models.CharField(max_length=100,default="Not Predicted")

    def __str__(self):
        return self.mail