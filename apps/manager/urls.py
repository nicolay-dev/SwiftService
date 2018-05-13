from django.conf.urls import url
from apps.manager.views import ManagerIndexView
from apps.restaurant.models import Restaurante
from apps.menu.views import CreateCategoria 
from apps.restaurant.views import CreateUser
from apps.manager.views import manager_index
from django.contrib.auth.views import login, logout_then_login
from django.contrib.auth.decorators import login_required

app_name = 'Manager'

urlpatterns = [

    # index usario final
    url(r'^(?P<slug>[-\w]+)/mesa-(?P<mesa_id>\d+)/$', ManagerIndexView.as_view(),name ='index'),
    
    # administración django DB
    # url(r'^login/', login, {'template_name': 'admin/login.html'}, name='login'),
    
    # de logeo
    url(r'^accounts/login/$', login, {'template_name': 'manager/login.html'}, name='login'),
    url(r'^manager/$', login_required(manager_index), name='index_manager'),
    url(r'^manager/crear_categoria/$', login_required(CreateCategoria.as_view()), name='create_categoria'),
    url(r'^manager/crear_usuario/$', login_required(CreateUser.as_view()), name='create_user'),
    # logout
    url(r'^logout/$', logout_then_login, name='logout'),


]
