from django.db import models
from apps.restaurant.models import Restaurante

# Create your models here.
# TODO: duplicidad en los datos: pueden agregar mas de una vez el mismo platillo al mismo combo
# TODO: Tipo -> Imagen por default
# TODO: se puede agregar una orden sin ningun platillo o combo
# TODO: Revisar los tipos de datos numericos ej: Oferta -> descuento
# TODO: Oferta -> establecer como se maneja y se guarda el formato del dia de la semna que se activa la oferta


class Tipo(models.Model):
    """Tipo: Especifica los tipos de platillo que se pueden ofrecer (Ej: Bebidas, Postres, Licor)"""
    # ForeignKeys
    restaurante = models.ForeignKey(Restaurante, blank=True, null=True, on_delete=models.CASCADE)
    # Attirbutes
    nombre = models.CharField(max_length=50)
    color = models.CharField(max_length=7, blank=False)
    imagen = models.ImageField(upload_to='images/tipos', blank=True, null=True)
    # imagen = models.ImageField(, default = 'pics_folder/None/no-img.jpg')

    def __str__(self):
        return '{}'.format(self.nombre)


class Platillo(models.Model):
    """Platillo: Especifica las caracteristicas de un platillo en concreto"""
    # Types
    TIPOS_TAMAÑO = {
        ('P', 'Pequeño'),
        ('M', 'Medio'),
        ('G', 'Grande'),
    }
    # ForeingKeys
    restaurante = models.ForeignKey(Restaurante, default = '1', null=False, blank=False, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo, blank=False, null=False, on_delete=models.CASCADE)
    # Attributes
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    precio = models.DecimalField(max_digits=9, decimal_places=2)
    tamaño = models.CharField(max_length=1, choices=TIPOS_TAMAÑO, blank=True, default='M')
    """tamaño : esto es un caracter que determina el tamaño del platillo de acuerdo a TPOS_TAMAÑO"""

    def __str__(self):
        return '{}'.format(self.nombre)


class Combo(models.Model):
    """Combo: Especifica las caracteristicas de un Combo en concreto"""
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=9, decimal_places=2)
    # TODO: revisas obligatoriedad descripción
    descripcion = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return '{}'.format(self.nombre)


class DetallesCombo(models.Model):
    """DetallesCombo : Tabla que almacena la relación de platillo y combo"""
    platillo = models.ForeignKey(Platillo, blank=False, null=False, on_delete=models.CASCADE)
    combo = models.ForeignKey(Combo, blank=False, null=False, on_delete=models.CASCADE)
    cantidad = models.IntegerField()


class Oferta(models.Model):
    """Oferta : Modelo que permite almacenar la información de los pedidos solicitados por los comensales"""
    # ForeignKeys
    tipo = models.ForeignKey(Tipo, blank=True, null=True, on_delete=models.CASCADE)
    platillo = models.ForeignKey(Platillo, blank=True, null=True, on_delete=models.CASCADE)
    combo = models.ForeignKey(Combo, blank=True, null=True, on_delete=models.CASCADE)
    # Attributes
    nombre = models.CharField(max_length=50, default='Oferta')
    descripcion = models.CharField(max_length=500)
    descuento = models.IntegerField()
    """descuento : Porcentaje de descuento"""
    # TODO: Revisar obligatoriedad en los campos de limite y dia
    limite = models.DateField()
    diaSemana = models.IntegerField()
    """diaSemana : representa el dia de la semana que se activa la oferta de acuerdo a un numero"""

    def __str__(self):
        return '{}'.format(self.nombre)


class Orden(models.Model):
    """Orden : Modelo que permite almacenar la información de los pedidos solicitados por los comensales"""
    # ForeignKeys
    oferta = models.ForeignKey(Oferta, blank=True, null=True, on_delete=models.CASCADE)
    # Attributes
    fechaHora = models.DateTimeField(auto_now=True)
    mesa = models.IntegerField()
    precioTotal = models.DecimalField(max_digits=9, decimal_places=2)


class DetallesOrden(models.Model):
    # ForeingKeys
    orden = models.ForeignKey(Orden, blank=False, null=False, on_delete=models.CASCADE)
    # TODO: verificar que por lo menos un platillo o un combo sea obligatorio
    platillo = models.ForeignKey(Platillo, blank=True, null=True, on_delete=models.CASCADE)
    combo = models.ForeignKey(Combo, blank=True, null=True, on_delete=models.CASCADE)
    # Attributes
    cantidad = models.IntegerField()
    infoAdicional = models.CharField(max_length=500)
    subTotal = models.DecimalField(max_digits=9, decimal_places=2)
