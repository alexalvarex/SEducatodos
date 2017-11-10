from django.conf.urls import (url, handler400, handler403, handler404, handler500 )
from . import views
from django.views.generic import TemplateView

urlpatterns = [
	url(r'^$', views.index, name='index'),
	# CENTROS
	url(r'^centros/$', views.all_centros_admin, name='all_centros_admin'),
	url(r'^centros/new/$', views.new_centro, name='new_centro'),
	url(r'^centros/new/add/$', views.new_centro_add, name='new_centro_add'),
	url(r'^centros/delete/(?P<pk>\d+)/$', views.delete_centro, name='delete_centro'),
	url(r'^centros/edit/(?P<pk>\d+)/$', views.edit_centro, name='edit_centro'),

]