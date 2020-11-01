from django.db import models

# Create your models here.
class Formulario(models.Model):
    nombre = models.CharField(max_length=200)
    pais = models.CharField(max_length=200)
    correo = models.CharField(max_length=200)
    asunto = models.CharField(max_length=200)
    mensaje = models.CharField(max_length=200) 