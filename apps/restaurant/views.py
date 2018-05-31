from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from apps.restaurant.models import Usuario
from apps.restaurant.forms import UserForm
from apps.menu.models import Tipo
from django.urls import reverse_lazy
# Create your views here.


class CreateUser(CreateView):
    model = User
    form_class = UserForm
    template_name = 'manager/user_form.html'
    success_url = reverse_lazy('Manager:index_manager')

class UserList(ListView):
    model = User
    template_name = 'manager/user_list.html'
    paginate_by = 5


class UserUpdate(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'manager/user_form.html'
    success_url = reverse_lazy('Manager:list_user')


class UserDelete(DeleteView):
    model = User
    template_name = 'manager/user_delete.html'
    success_url = reverse_lazy('Manager:list_user')



