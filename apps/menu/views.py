# functions
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# views
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# model
from apps.menu.models import Tipo, Platillo
from apps.restaurant.models import Restaurante
# formulatios
from apps.menu.forms import MenuForm
# ajax
from django_ajax.decorators import ajax
from django.http import JsonResponse, HttpResponse
#para serializar en json un objeto
from django.core import serializers

from django.urls import reverse_lazy

from collections import defaultdict
import copy
# Create your views here.

@ajax
@csrf_exempt
def get_platillo(request, *args,**kwargs):
    # import pdb;pdb.set_trace()
    platillo_pk = request.POST.get('getData')
    serialized_platillo = serializers.serialize('json', [Platillo.objects.get(id=platillo_pk),])
    data = {
        'getData': serialized_platillo
    }
    return JsonResponse(data)


@csrf_exempt
def add_platillo(request, *args, **kwargs):
    platillo = request.POST.get('getData')
    # # del request.session['platillo_1']
    # import pdb;pdb.set_trace()
    cadena = "platillo" + "_" + str(len(request.session.keys()) - 3)
    request.session[cadena] = platillo

    # llaves = request.session.keys()
    # for key in llaves:
    #     if "platillo_" in key:
    #         del request.session[key]

    return JsonResponse("Nicolay", safe=False)


@csrf_exempt
def clean_cart(request, *args, **kwargs):
    llaves = request.session.keys()
    lista_keys = []
    for key in llaves:
        if "platillo_" in key:
            lista_keys.append(key)
    for key in lista_keys:
            del request.session[key]
    return JsonResponse("Nicolay", safe=False)


@csrf_exempt
def load_sesion(request, *args, **kwargs):
    llaves = request.session.keys()
    lista_platillos = []
    for key in llaves:
        if "platillo_" in key:
            lista_platillos.append(request.session[key])


    # serialized_platillos = serializers.serialize('json',lista_keys)
    data = {
        'getData': lista_platillos
    }
    return JsonResponse(data)

class CreateCategoria(CreateView):
    model = Tipo
    form_class = MenuForm
    template_name = 'manager/menu_form.html'
    success_url = reverse_lazy('Manager:index_manager')

class CategoriaList(ListView):
    model = Tipo
    template_name = 'manager/type_list.html'
    paginate_by = 5

class CategoriaUpdate(UpdateView):
    model = Tipo
    form_class = MenuForm
    template_name = 'manager/menu_form.html'
    success_url = reverse_lazy('Manager:list_categoria')

class CategoriaDelete(DeleteView):
    model = Tipo
    template_name = 'manager/type_delete.html'
    success_url = reverse_lazy('Manager:list_categoria')

class MenuListView(ListView):
    model = Tipo
    template_name = 'menu/menuList.html'


    
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





# class LoadPlatillo(DetailView):
#     model = Platillo
#     context_object_name = 'platillo'
#     template_name = 'menu/loadPlatillo.html'

#     def post(data):
#         return render();
