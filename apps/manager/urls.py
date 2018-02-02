from django.conf.urls import url
from apps.manager.views import ManagerIndexView
from apps.restaurant.models import Restaurante

app_name = 'Manager'

urlpatterns = [
    
    # url(r'^(?P<pk>\d+)/$', ManagerIndexView.as_view(), name='index'),
    url(r'^(?P<slug>[-\w]+)/mesa-(?P<mesa_id>\d+)/$',
        ManagerIndexView.as_view(), name='index'),
]
