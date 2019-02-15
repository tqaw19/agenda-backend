from django.conf.urls import url
from agenda import views

urlpatterns = [
    url(r'^agenda/$', views.usuario_list),
    url(r'^agenda/(?P<pk>[0-9]+)/$', views.usuario_detail),
]