from django.conf.urls import url
from apps.manager.views import ManagerIndexView
from apps.restaurant.models import Restaurante
from apps.menu.views import CreateCategoria, CategoriaUpdate, CategoriaList, CategoriaDelete
from apps.restaurant.views import CreateUser, UserList, UserUpdate, UserDelete
from apps.manager.views import manager_index, qr_cretate, order_list
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
    url(r'^manager/listar_categorias', login_required(CategoriaList.as_view()), name='list_categoria'),
    url(r'^manager/crear_categoria/$', login_required(CreateCategoria.as_view()), name='create_categoria'),
    url(r'^manager/editar_categoria/(?P<pk>\d+)/$', login_required(CategoriaUpdate.as_view()), name='update_categoria'),
    url(r'^manager/eliminar_categoria/(?P<pk>\d+)/$', login_required(CategoriaDelete.as_view()), name='delete_categoria'),
    url(r'^manager/listar_usuarios', login_required(UserList.as_view()), name='list_user'),
    url(r'^manager/crear_usuario/$', login_required(CreateUser.as_view()), name='create_user'),
    url(r'^manager/editar_usuario/(?P<pk>\d+)/$', login_required(UserUpdate.as_view()), name='update_user'),
    url(r'^manager/eliminar_usuario/(?P<pk>\d+)/$', login_required(UserDelete.as_view()), name='delete_user'),
    url(r'^manager/generar_qr/$', login_required(qr_cretate), name='generate_qr'),
    url(r'^manager/ordenes/$', login_required(order_list), name='list_order'),
    # url(r'^manager/generar_qr/(?P<slug>[-\w]+)/)/$', login_required(qr_cretate), name='index'),
    # logout
    url(r'^logout/$', logout_then_login, name='logout'),


]
