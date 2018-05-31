from django.conf.urls import url
from apps.menu.views import MenuListView, get_platillo, add_platillo, clean_cart, load_sesion
from apps.restaurant.models import Restaurante
from django.views.decorators.csrf import csrf_exempt

app_name = 'Menu'

urlpatterns = [

    # url(r'^(?P<pk>\d+)/$', ManagerIndexView.as_view(), name='index'),
    url(r'^menu/$', MenuListView.as_view(), name='menuList'),
    # ajax
    url(r'^menu/ajax/get_platillo/$',
        csrf_exempt(get_platillo), name='loadPlatillo'),
    # getPlatillos
    url(r'^menu/ajax/save_to_cart/$', csrf_exempt(add_platillo), name='saveToCart'),
    # cleancart
    url(r'^menu/ajax/clean_cart/$', csrf_exempt(clean_cart), name='cleanCart'),
    # loadSesion
    url(r'^menu/ajax/load_sesion/$', csrf_exempt(load_sesion), name='loadSesion'),
]
