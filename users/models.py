from django.db import models

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Create your models here.
class UsuarioManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        """
        Crea y guarda un error dado un email y una contraseña
        """
        if not email:
            raise ValueError("Debe ingresa un email")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        """
        Crea un superusuario con un correo y password dados
        """

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Superuser debe tener  is_staff = True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(('Super user debe tener is_superuser=True'))
        return self.create_user(email, password, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('Correo Electronico', unique=True)
    nombres = models.CharField('Nombres', max_length=255, blank=True, null=True)
    apellidos = models.CharField('Apellidos', max_length=255, blank=True, null=True)
    telefono = models.CharField('Telefono', max_length=10, null=True, blank=True)
    direccion = models.CharField('Dirección', max_length=255, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add = True)

    objects =  UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
    
    def __str__(self):
        return f"Email Usuario: {self.email}"

    def nombre_completo(self):
        nombres = ''
        if self.nombres is not None:
            nombres += self.nombres
        if self.apellidos is not None:
            nombres += f" {self.apellidos}"
        return nombres
