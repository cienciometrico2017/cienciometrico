from django.db import models

# Create your models here.
class Evento(models.Model):
    nombre= models.CharField(max_length=50)
    lugar= models.CharField(max_length=70)
    fecha= models.DateField()
