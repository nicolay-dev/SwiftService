from django.shortcuts import render
from django.views.generic import ListView
from apps.menu.models import Tipo, Platillo
from apps.restaurant.models import Restaurante
# Create your views here.

class MenuListView(ListView):
    model = Tipo
    template_name = 'menu/menuList.html'

    # def __init__(self,**kwargs):
    #     self.restaurante = super(MenuListView, self).get_context_data(**kwargs)
    #     pass

    # def get(self, request, *args, **kwargs):
    #     self.restaurante = Restaurante.objects.get(
    #         slug=kwargs['slug'])
    #     pass

    def get_queryset(self, *args, **kwargs):
        # import pdb;pdb.set_trace()
        self.restaurante = Restaurante.objects.get(slug=self.kwargs['slug'])
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
        context['restaurante_desc'] = self.restaurante.descMenu
        context['object_list'] = Platillo.objects.filter(
            restaurante__slug=self.restaurante.slug)
        return context
