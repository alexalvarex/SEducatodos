from django.conf.urls import (url, handler400, handler403, handler404, handler500 )
from . import views
from django.views.generic import TemplateView

handler400 = 'adminapp.views.bad_request'
handler403 = 'adminapp.views.permission_denied'
handler404 = 'adminapp.views.page_not_found'
handler500 = 'adminapp.views.server_error'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^alumnos/$', views.alumnosxgrado, name='alumnosxgrado'),
	url(r'^alumnos/all/$', views.alumnos_sinmat, name='alumnos_sinmat'),
	url(r'^alumnos/grado/(?P<pk>\d+)/$', views.all_students, name='all_students'),
	url(r'^alumnos/new/$', views.new_student, name='new_student'),
	url(r'^alumnos/new/add/$', views.new_student_add, name='new_student_add'),
	url(r'^alumnos/familiar/(?P<pk>\d+)/all/$', views.all_familiar, name='all_familiar'),
	url(r'^alumnos/familiar/(?P<pk>\d+)/$', views.new_familiar, name='new_familiar'),
	url(r'^alumnos/familiar/add/$', views.new_familiar_add, name='new_familiar_add'),
	url(r'^promotores/$', views.all_promotores, name='all_promotores'),
	url(r'^promotores/new/$', views.new_promotor, name='new_promotor'),
	url(r'^promotores/new/add/$', views.new_promotor_add, name='new_promotor_add'),
	url(r'^promotores/edit/(?P<pk>\d+)/$', views.edit_promotores, name='edit_promotores'),
	url(r'^promotores/delete/(?P<pk>\d+)/$', views.delete_promotor, name='delete_promotor'),
	url(r'^facilitador/$', views.all_facilitador, name='all_facilitador'),
	url(r'^facilitador/new/$', views.new_facilitador, name='new_facilitador'),
	url(r'^facilitador/new/add/$', views.new_facilitador_add, name='new_facilitador_add'),
	url(r'^facilitador/delete/(?P<pk>\d+)/$', views.delete_facilitador, name='delete_facilitador'),
	url(r'^facilitador/edit/(?P<pk>\d+)/$', views.edit_facilitador, name='edit_facilitador'),
	url(r'^grados/$', views.all_grados, name='all_grados'),
	url(r'^grados/new/$', views.new_grado, name='new_grado'),
	url(r'^grados/new/add/$', views.new_grado_add, name='new_grado_add'),
	url(r'^grados/delete/(?P<pk>\d+)/$', views.delete_grado, name='delete_grado'),
	url(r'^grados/edit/(?P<pk>\d+)/$', views.edit_grado, name='edit_grado'),
	url(r'^centros/$', views.all_centros, name='all_centros'),
	
	url(r'^enroll/new/$', views.new_enroll, name='new_enroll'),
	url(r'^enroll/massive/$', views.enroll_massive, name='enroll_massive'),
	url(r'^enroll/massive/add/$', views.enroll_massive_add, name='enroll_massive_add'),
	url(r'^enroll/all/$', views.all_enroll, name='all_enroll'),
	url(r'^enroll/new/add/$', views.new_enroll_add, name='new_enroll_add'),
	url(r'^enroll/new/alumno/(?P<pk>\d+)/$', views.matricularxalumno, name='matricularxalumno'),
	url(r'^enroll/new/alumno/add/$', views.matricularxalumno_add, name='matricularxalumno_add'),
	url(r'^reports/$', views.all_reports, name='all_reports'),
	url(r'^reports/graphics$', views.all_graphics, name='all_graphics'),
	url(r'^reports/fisico/$', views.reportes ,name="reportes"),
	url(r'^notas/$', views.notas ,name="notas"),
	url(r'^descargas/$', views.descargas ,name="descargas"),
	url(r'^tombola/$', views.tombola ,name="tombola"),

]