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
)