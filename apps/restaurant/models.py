from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.


class Restaurante(models.Model):
    """ Restaurante : Modelo que permite almacenar toda la información de los restaurantes"""
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    email = models.EmailField()
    slug = models.CharField(max_length=200, blank=True, editable=False, unique=True)
    # subdominio = models.CharField(max_length=100)
    descMenu = models.CharField(max_length=500)
    n_mesas = models.IntegerField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Restaurante, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.nombre)


class Usuario(models.Model):
    """ Usuario : Modelo que permite almacenar toda la información de los Usuarios"""
    # Types
    TIPOS_USUARIO = {
        ('V', 'Visitante'),
        ('A', 'Autentificado'),
        ('E', 'Editor'),
        ('R', 'Administrador'),
    }
    # ForeingKeys
    restaurante = models.ForeignKey(Restaurante, null=False, blank=False, on_delete=models.CASCADE)
    # Attributes
    nombre = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=40)
    """contraseña : esto es un sha que se almacena en varchar(40)"""
    tipo = models.CharField(max_length=1, choices=TIPOS_USUARIO)
    """tipo : esto es un caracter que determina el tipo de usuarios de acuerdo a TPOS_USUARIOS"""

    def __str__(self):
        return '{}'.format(self.nombre)
