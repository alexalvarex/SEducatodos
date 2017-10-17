from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^login/$', views.log_in, name='login'),
	url(r'^login/error/$', views.log_in_error, name='login_error'),
	url(r'^login/inactive/$', views.log_in_inactive, name='login_inactive'),
	url(r'^logout/$', views.log_out, name='logout'),
	url(r'^myprofile/$', views.myprofile, name='myprofile'),
	url(r'^changepass/$', views.changepass, name='changepass'),
	url(r'^forgotpass/$', views.forgotpass, name='forgotpass'),
	url(r'^blockscreen/$', views.blockscreen, name='blockscreen'),
]