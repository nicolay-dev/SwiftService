from django.conf.urls import url
from apps.menu.views import MenuListView
from apps.restaurant.models import Restaurante

app_name = 'Menu'

urlpatterns = [

    # url(r'^(?P<pk>\d+)/$', ManagerIndexView.as_view(), name='index'),
    url(r'^menu/$', MenuListView.as_view(), name='menuList'),
]
