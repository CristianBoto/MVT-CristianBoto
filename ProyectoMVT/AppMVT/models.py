from datetime import datetime
from django.db import models

class HIJO(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField()
    fecha= models.DateField()    

class PAPA(models.Model):
     nombre= models.CharField(max_length=50)
     apellido= models.CharField(max_length=50)
     email= models.EmailField()
     profesion= models.CharField(max_length=50)

class MAMA(models.Model):
     nombre= models.CharField(max_length=50)
     apellido= models.CharField(max_length=50)
     email= models.EmailField()
     profesion= models.CharField(max_length=50)

