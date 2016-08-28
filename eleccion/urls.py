from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'GestorElectoral.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

#    url(r'^$', views.index, name='index'),
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^login/$', views.Login, name='login'),
    url(r'^logout/$', views.Logout, name='logout'),
    url(r'^circunscripcion/$', views.CircunscripcionLista.as_view(), name='circunscripcion_url'),
    url(r'^circunscripcion/crear/$', views.CircunscripcionCrear.as_view(), name='circunscripcion_crear_url'),
    url(r'^circunscripcion/vistaDetallada/(?P<pk>.*)$', views.CircunscripcionDetalle.as_view(), name='circunscripcion_detalle_url'),


)