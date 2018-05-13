from django.shortcuts import render
from django.views.generic import CreateView
from apps.restaurant.models import Usuario
from apps.restaurant.forms import UserForm
from django.urls import reverse_lazy
# Create your views here.


class CreateUser(CreateView):
    model = Usuario
    form_class = UserForm
    template_name = 'manager/menu_form.html'
    success_url = reverse_lazy('Manager:index_manager')
