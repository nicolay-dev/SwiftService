from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from apps.restaurant.models import Restaurante


# Create your views here.

# def save_session(request, id_mesa):
#     request.session["mesa"] = id_mesa
#     render(request, 'index.html', request.session)
#     return redirect('Manager:index')

class ManagerIndexView(DetailView):
    model = Restaurante
    template_name = 'index.html'
    context_object_name = 'restaurante'
    # request.session['fav_color'] = 'blue'
    
    def get_context_data(self, **kwargs):
        # import pdb;pdb.set_trace()        
        context = super(ManagerIndexView, self).get_context_data(**kwargs)
        # del self.request.session['mesa']
        # del self.request.session['slug_restaurante']
        self.request.session['mesa_id'] = self.kwargs.get('mesa_id')
        self.request.session['restaurante_slug'] = self.object.slug
        self.request.session['restaurante_nombre'] = self.object.nombre
        context['mesa_id'] = self.request.session['mesa_id']
        context['restaurante_slug'] = self.request.session['restaurante_slug']
        context['restaurante_nombre'] = self.request.session['restaurante_nombre']
        return context
