from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UsuarioManager(BaseUserManager):
    def create_user(self, identificacion, nombre, email, rol, contrasena=None, **extra_fields):
        if not identificacion:
            raise ValueError('El usuario debe tener una identificación')
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')
        user = self.model(identificacion=identificacion, nombre=nombre, email=email, rol=rol, **extra_fields)
        if contrasena:
            user.set_password(contrasena)
        user.save(using=self._db)
        return user

    def create_superuser(self, identificacion, nombre, email, contrasena=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True.')
        return self.create_user(identificacion, nombre, email, rol=1, contrasena=contrasena, **extra_fields)

class Usuario(AbstractBaseUser):
    identificacion = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    contrasena = models.CharField(max_length=255)  # Sin valor predeterminado
    rol = models.IntegerField(choices=[(1, 'Administrador'), (2, 'Gerente'), (3, 'Usuario regular')])  # Etiquetas descriptivas
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = UsuarioManager()

    USERNAME_FIELD = 'identificacion'
    REQUIRED_FIELDS = ['nombre', 'email']  # Quitando 'rol' de los campos requeridos

    def __str__(self):
        return self.nombre

