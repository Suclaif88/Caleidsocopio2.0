from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    identificacion = models.IntegerField()
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    contrasena = models.CharField(max_length=255)
    rol = models.IntegerField()
    last_login = models.DateTimeField(blank=True, null=True)

