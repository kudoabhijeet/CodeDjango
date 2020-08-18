from django.db import models
from django.core.validators import (
    EmailValidator,
)

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 100)
    address = models.TextField(null= True)
    phone  = models.CharField(max_length = 15)
    
    def __str__(self):
        return self.name
