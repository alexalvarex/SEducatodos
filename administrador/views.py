from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from adminapp.models import *
from django.db.models import Count
from datetime import datetime
from reportlab.pdfgen import canvas
from cStringIO import StringIO
from io import BytesIO
from django.conf import settings
from django.views.generic import View
from django.http import Http404  

from django.contrib.auth.models import User

# Create your views here.

@login_required()
def index(request):
	if request.user.is_staff:
		return render(request, 'index.html')
	else:
		return render(request, '404.html')

# CENTROS
@login_required()
def all_centros_admin(request):
	if request.user.is_staff:
		centros = Centro.objects.all()
		numc = centros.count()
		return render(request, 'all_centros.html', {'centros':centros, 'numc':numc})
	else:
		return render(request, '404.html')

@login_required()
def new_centro(request):
	if request.user.is_staff:
		patro = Patrocinador.objects.all()
		zona = Zona.objects.all()
		des = Descicion.objects.all()
		tp = TipoPersona.objects.get(pk = 2)
		promotor = Persona.objects.filter(tipo_persona = tp)
		municholu = Municipio.objects.filter(depto = 1)
		munivalle = Municipio.objects.filter(depto = 2)
		return render(request, 'new_centro.html', {'des':des, 'patro':patro, 'zona':zona, 
			'promo': promotor, 'cholu': municholu, 'valle': munivalle})
	else:
		return render(request, '404.html')

@login_required()
def new_centro_add(request):
	if request.user.is_staff:
		if request.method == 'POST':
			try:
				centro = request.POST.get('centro')
				tipoc = request.POST.get('tipoc')
				patro = request.POST.get('patro')
				zona = request.POST.get('zona')
				patro_recibe = request.POST.get('patro_recibe')
				que = request.POST.get('que')
				cuando = request.POST.get('cuando')
				promo = request.POST.get('promo')
				donde = request.POST.get('donde')
				direccion = request.POST.get('direccion')
				muni = request.POST.get('muni')
				quien = request.POST.get('quien')

				municipio = Municipio.objects.get(pk = muni)
				tc = TipoCentro.objects.get(pk = tipoc)
				pat = Patrocinador.objects.get(pk = patro)
				zon = Zona.objects.get(pk = zona)
				pi = Descicion.objects.get(pk = patro_recibe)
				prom = Personas.objects.get(pk = promo)

				centro = Centro(
						centro = centro,
						tipo_centro = tc,
						patrocinador = pat,
						zona = zon,
						patro_incentivo = pi,
						patro_recibe = que,
						cada_cuando = cuando,
						quien = quien,
						promotor = prom,
						donde_funciona = donde,
						direccion = direccion,
						municipio = municipio)
				centro.save()
				return HttpResponseRedirect('/administrador/centros/')
			except Exception as e:
				return HttpResponse(e)
	else:
		return render(request, '404.html')

@login_required()
def delete_centro(request, pk):
	if request.user.is_staff:
		centro = Centro.objects.get(pk = pk)
		try:
			centro.delete()
			return HttpResponseRedirect('/administrador/centros/')
		except Exception, e:
			return HttpResponse(e)
	else:
		return render(request, '404.html')

@login_required()
def edit_centro(request, pk):
	if request.user.is_staff:
		if request.method == 'POST':
			centro = request.POST.get('centro')
			tipoc = request.POST.get('tipoc')
			patro = request.POST.get('patro')
			zona = request.POST.get('zona')
			patro_recibe = request.POST.get('patro_recibe')
			que = request.POST.get('que')
			cuando = request.POST.get('cuando')
			promo = request.POST.get('promo')
			donde = request.POST.get('donde')
			direccion = request.POST.get('direccion')

			tc = TipoCentro.objects.get(pk = tipoc)
			pat = Patrocinador.objects.get(pk = patro)
			zon = Zona.objects.get(pk = zona)
			pi = Descicion.objects.get(pk = patro_recibe)
			prom = Personas.objects.get(pk = promo)

			F = Centro.objects.get(pk=pk)
			F.centro = centro
			F.tipo_centro = tc
			F.patrocinador = pat
			F.zona = zon
			F.patro_incentivo = pi
			F.patro_recibe = que
			F.cada_cuando = cuando
			F.promotor = prom
			F.donde_funciona = donde
			F.direccion = direccion
			F.save()
		return HttpResponseRedirect('/administrador/centros/')
	else:
		return render(request, '404.html')