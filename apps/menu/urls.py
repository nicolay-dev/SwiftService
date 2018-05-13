from django.conf.urls import url
from apps.menu.views import MenuListView, get_platillo, add_platillo, clean_cart, load_sesion
from apps.restaurant.models import Restaurante

app_name = 'Menu'

urlpatterns = [

    # url(r'^(?P<pk>\d+)/$', ManagerIndexView.as_view(), name='index'),
    url(r'^menu/$', MenuListView.as_view(), name='menuList'),
    # ajax
    url(r'^menu/ajax/get_platillo/$', get_platillo, name='loadPlatillo'),
    # getPlatillos
    url(r'^menu/ajax/save_to_cart/$', add_platillo, name='saveToCart'),
    # cleancart
    url(r'^menu/ajax/clean_cart/$', clean_cart, name='cleanCart'),
    # loadSesion
    url(r'^menu/ajax/load_sesion/$', load_sesion, name='loadSesion'),
]
