from django.contrib import admin
from apps.menu.models import Tipo, Platillo, Combo, DetallesCombo, Oferta, Orden, DetallesOrden

# Register your models here.
admin.site.register(Tipo)
admin.site.register(Platillo)
admin.site.register(Combo)
admin.site.register(DetallesCombo)
admin.site.register(Oferta)
admin.site.register(Orden)
admin.site.register(DetallesOrden)
