from django.shortcuts import render
from django.views.generic import ListView
from apps.menu.models import Tipo, Platillo
from apps.restaurant.models import Restaurante
# Create your views here.

class MenuListView(ListView):
    model = Tipo
    template_name = 'menu/menuList.html'

    def __init__(self, *args, **kwargs):
        import pdb;pdb.set_trace()
        nico = super(MenuListView, self).get_context_data(**kwargs)
        self.restaurante = Restaurante.objects.get(slug=self.kwargs.get('slug'))
        return

    def get_queryset(self):
        return Tipo.objects.filter(
            restaurante__slug=self.restaurante.slug)

    def get_context_data(self, **kwargs):
        # sesión
        self.request.session['mesa_id'] = self.kwargs.get('mesa_id')
        self.request.session['restaurante_slug'] = self.restaurante.slug
        self.request.session['restaurante_nombre'] = self.restaurante.nombre

        # contexto
        context = super(MenuListView, self).get_context_data(**kwargs)
        context['mesa_id'] = self.kwargs.get('mesa_id')
        context['restaurante_slug'] = self.restaurante.slug
        context['restaurante_nombre'] = self.restaurante.nombre
        context['restaurante_desc'] = self.restaurante.slug
        context['object_list'] = Platillo.objects.filter(
            restaurante__slug=self.restaurante.slug)
        return context
