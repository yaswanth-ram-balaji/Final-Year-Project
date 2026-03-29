from django.db import models

# Create your models here. 
class Register(models.Model):
    name = models.CharField(max_length=55)
    email = models.EmailField(max_length=55)
    password = models.CharField(max_length=55)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
