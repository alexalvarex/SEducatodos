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
from django.db.models import Q 

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
def centrosxdepto(request):
	if request.user.is_staff:
		deptos = Depto.objects.all()
		return render(request, 'centrosxdepto.html', {'deptos':deptos})
	else:
		return render(request, '404.html')


@login_required()
def all_centros_admin(request, pk):
	if request.user.is_staff:
		depto = Depto.objects.get(pk = pk)
		muni = Municipio.objects.filter(depto = depto).values_list('depto_id', flat=True)

		lista_cholu = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
		lista_valle = [17,18,19,20,21,22,23,24,25]
		centros = Centro.objects.all()
	 	centros_cholu = centros.exclude(municipio__in=lista_valle)
	 	centros_valle = centros.exclude(municipio__in=lista_cholu)

		numc = centros_cholu.count()
		numv = centros_valle.count()
		return render(request, 'all_centros.html', {'centros_cholu':centros_cholu, 'centros_valle':centros_valle, 
			'numc':numc, 'numv':numv, 'depto': depto})
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
				patro = request.POST.get('patro')
				zona = request.POST.get('zona')
				patro_recibe = request.POST.get('patro_recibe')
				que = request.POST.get('que')
				cuando = request.POST.get('cuando')
				promo = request.POST.get('promo')
				nombrepromo = request.POST.get('nombrepromo')
				donde = request.POST.get('donde')
				direccion = request.POST.get('direccion')
				muni = request.POST.get('muni')
				quien = request.POST.get('quien')

				municipio = Municipio.objects.get(pk = muni)
				pat = Patrocinador.objects.get(pk = patro)
				zon = Zona.objects.get(pk = zona)
				pi = Descicion.objects.get(pk = patro_recibe)
				prom = Descicion.objects.get(pk = promo)

				centro = Centro(
						centro = centro,
						patrocinador = pat,
						zona = zon,
						patro_incentivo = pi,
						patro_recibe = que,
						quien = quien,
						cada_cuando = cuando,
						promotor = prom,
						nombre_promotor = nombrepromo,
						donde_funciona = donde,
						direccion = direccion,
						municipio = municipio)
				centro.save()
				return HttpResponseRedirect(reverse('all_centros_admin', args=[municipio.depto.id]))
			except Exception as e:
				return HttpResponse(e)
	else:
		return render(request, '404.html')

@login_required()
def editar_centros(request, pk):
	if request.user.is_staff:
		centro = Centro.objects.get(pk = pk)
		patro = Patrocinador.objects.all()
		zona = Zona.objects.all()
		des = Descicion.objects.all()
		tp = TipoPersona.objects.get(pk = 2)
		promotor = Persona.objects.filter(tipo_persona = tp)
		municholu = Municipio.objects.filter(depto = 1)
		munivalle = Municipio.objects.filter(depto = 2)
		return render(request, 'editar_centros.html', {'des':des, 'patro':patro, 'zona':zona, 
			'promo': promotor, 'cholu': municholu, 'valle': munivalle, 'centro':centro})
	else:
		return render(request, '404.html')

@login_required()
def editar_centros_add(request):
	if request.user.is_staff:
		if request.method == 'POST':
			try:
				pk = request.POST.get('id')
				centro = request.POST.get('centro')
				patro = request.POST.get('patro')
				zona = request.POST.get('zona')
				patro_recibe = request.POST.get('patro_recibe')
				que = request.POST.get('que')
				cuando = request.POST.get('cuando')
				promo = request.POST.get('promo')
				nombrepromo = request.POST.get('nombrepromo')
				donde = request.POST.get('donde')
				direccion = request.POST.get('direccion')
				muni = request.POST.get('muni')
				quien = request.POST.get('quien')

				municipio = Municipio.objects.get(pk = muni)
				pat = Patrocinador.objects.get(pk = patro)
				zon = Zona.objects.get(pk = zona)
				pi = Descicion.objects.get(pk = patro_recibe)
				prom = Descicion.objects.get(pk = promo)

				ce = Centro.objects.get(pk = pk)
				ce.centro = centro
				ce.patrocinador = pat
				ce.zona = zon
				ce.patro_incentivo = pi
				ce.patro_recibe = que
				ce.quien = quien
				ce.cada_cuando = cuando
				ce.promotor = prom
				ce.nombre_promotor = nombrepromo
				ce.donde_funciona = donde
				ce.direccion = direccion
				ce.municipio = municipio
				ce.save()
				return HttpResponseRedirect(reverse('all_centros_admin', args=[municipio.depto.id]))
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
			return HttpResponseRedirect(reverse('all_centros_admin', args=[centro.municipio.depto.id]))
		except Exception, e:
			return HttpResponse(e)
	else:
		return render(request, '404.html')

@login_required()
def facilitadorxcentro(request, pk):
	if request.user.is_staff:
		centro = Centro.objects.get(pk = pk)
		facilitadores = Facilitador.objects.filter(centro = centro)
		numf = facilitadores.count()
		return render(request, 'facilitadores.html', {'data':facilitadores, 'centro':centro, 'numf':numf})
	else:
		return render(request, '404.html')

@login_required()
def perfil(request):
	if request.user.is_staff:
		perfil = Administrador.objects.get(usuario = request.user)
		numa = Administrador.objects.all().count()
		return render(request, 'perfil.html', {'data':perfil, 'numa': numa})
	else:
		return render(request, '404.html')

@login_required()
def editar_perfil(request, pk):
	if request.user.is_staff:
		perfil = Administrador.objects.get(pk = pk)
		formacion = FormacionAcademica.objects.all()
		sexo = Sexo.objects.all()
		cholu = Municipio.objects.filter(depto = 1)
		valle = Municipio.objects.filter(depto = 2)
		return render(request, 'editar_perfil.html', {'data':perfil,'formacion':formacion,
			'sexo':sexo,'cholu':cholu, 'valle':valle})
	else:
		return render(request, '404.html')

@login_required()
def editar_perfil_add(request):
	if request.user.is_staff:
		if request.method == 'POST':
			try:
				pk = request.POST.get('id')
				numid = request.POST.get('numid')
				nombre = request.POST.get('nombre')
				apellido = request.POST.get('apellido')
				direccion = request.POST.get('direccion')
				muni = request.POST.get('muni')
				telefono = request.POST.get('telefono')
				lugart = request.POST.get('lugart')
				ocupacion = request.POST.get('ocupacion')
				formacion = request.POST.get('formacion')
				otra_fomacion = request.POST.get('otro')
				fechan = request.POST.get('fechan')
				edad = request.POST.get('edad')
				genero = request.POST.get('sexo')
				correo = request.POST.get('correo')

				municipio = Municipio.objects.get(pk = muni)
				formacion_academica = FormacionAcademica.objects.get(pk = formacion)
				sexo = Sexo.objects.get(pk = genero)

				admin = Administrador.objects.get(pk = pk)

				admin.numid = numid
				admin.nombre = nombre
				admin.apellido = apellido
				admin.domicilio = direccion
				admin.municipio = municipio
				admin.telefono = telefono
				admin.lugar_trabajo = lugart
				admin.ocupacion = ocupacion
				admin.formacion_academida = formacion_academica
				admin.otra_formacion = otra_fomacion
				admin.fecha_nacimiento = fechan
				admin.edad = edad
				admin.sexo = sexo
				admin.correo = correo
				admin.save()

				return HttpResponseRedirect(reverse('perfil'))
			except Exception as e:
				return HttpResponse(e)
	else:
		return render(request, '404.html')

@login_required()
def configuracion(request):
	if request.user.is_staff:
		periodo = Periodo.objects.all()
		metodo = Metodologia.objects.all()
		centro = Centro.objects.all()
		config = Configuracion.objects.latest('id')
		return render(request, 'config.html', {'metodo':metodo, 'periodo':periodo, 'centro':centro, 'config':config})
	else:
		return render(request, '404.html')

@login_required()
def configuracion_add(request):
	if request.user.is_staff:
		if request.method == 'POST':
			try:
				centros = request.POST.getlist('centro[]')
				anio = request.POST.get('anio')
				metodo = request.POST.get('metodo')
				periodo = request.POST.get('periodo')
				fechai = request.POST.get('fechai')
				fechaf = request.POST.get('fechaf')

				m = Metodologia.objects.get(pk = metodo)

				pe = Periodo.objects.create(
					num_periodo = periodo,
					inicio_clases = fechai,
					fin_clases = fechaf	
					)

				c = Configuracion(
					anio_lectivo = anio,
					metodo = m,
					periodo = pe
					)
				c.save()

				for a in centros:
					cen = Centro.objects.get(pk = a)
					c.centro.add(cen)

				return HttpResponseRedirect(reverse('config'))
			except Exception as e:
				return HttpResponse(e)
	else:
		return render(request, '404.html')

@login_required()
def gradosxfacilitador(request, pk, pk2):
	if request.user.is_staff:
		facilitador = Facilitador.objects.get(pk = pk)
		centro = Centro.objects.get(pk = pk2)
		grados = Grado.objects.filter(facilitador = facilitador)
		numg = grados.count()
		return render(request, 'gradosxfacilitador.html', {'centro':centro,'grados':grados, 'numg': numg, 'facilitador':facilitador})
	else:
		return render(request, '404.html')

@login_required()
def alumnos(request, pk):
	if request.user.is_staff:
		grado = Grado.objects.get(pk = pk)
		alumnos = Matricula.objects.filter(grado = pk)
		numg = alumnos.count()
		return render(request, 'alumnos.html', {'data':alumnos, 'numg':numg, 'grado':grado})
	else:
		return render(request, '404.html')

@login_required()
def alumnossinmat(request):
	if request.user.Facilitador:
		alumno = Alumno.objects.all()
		matri = Matricula.objects.all().values_list('persona_id', flat=True)
		alumnos = alumno.exclude(id__in = matri)
		numu = alumnos.count()
		return render(request, 'alumnossinmat.html', {'data':alumnos})
	else:
		return render(request, '404.html')

@login_required()
def alumnonuevo(request):
	if request.user.is_staff:
		sexo = Sexo.objects.all()
		ge = GrupoEtnico.objects.all()
		cholu = Municipio.objects.filter(depto = 1)
		valle = Municipio.objects.filter(depto = 2)
		des = Descicion.objects.all()
		user = User.objects.all()
		return render(request, 'alumnonuevo.html', {'user':user,'ge':ge, 'des':des, 'sexo':sexo, 'cholu':cholu, 'valle':valle})
	else:
		return render(request, '404.html')

@login_required()
def alumnonuevo_add(request):
	if request.user.is_staff:
		if request.method == 'POST':
			try:
				numid = request.POST.get('numid')
				nombre = request.POST.get('nombre')
				apellido = request.POST.get('apellido')
				direccion = request.POST.get('direccion')
				muni = request.POST.get('muni')
				ge = request.POST.get('ge')
				mu = Municipio.objects.get(pk = muni)
				grupoe = GrupoEtnico.objects.get(pk = ge)
				tel = request.POST.get('telefono')
				fechan = request.POST.get('fechan')
				edad = request.POST.get('edad')
				trabaja = request.POST.get('trabaja')
				des = Descicion.objects.get(pk = trabaja)
				ocupacion = request.POST.get('ocupacion')
				sex =  request.POST.get('sexo')
				sexo = Sexo.objects.get(pk = sex)

				persona = Alumno(
						numid = numid, 
						nombre = nombre,
						apellido = apellido,
						municipio = mu,
						domicilio = direccion,
						telefono = tel,
						sexo = sexo,
						grupo_etnico = grupoe,
						trabaja = des,
						ocupacion = ocupacion,
						fecha_nacimiento = fechan,
						edad = edad)
				persona.save()
				return HttpResponseRedirect('/administrador/alumnos/new/')
			except Exception as e:
				return HttpResponse(e)
	else:
		return render(request, '404.html')

@login_required()
def editar_alumno(request, pk):
	if request.user.is_staff:
		sexo = Sexo.objects.all()
		ge = GrupoEtnico.objects.all()
		cholu = Municipio.objects.filter(depto = 1)
		valle = Municipio.objects.filter(depto = 2)
		des = Descicion.objects.all()
		alumno = Alumno.objects.get(pk = pk)
		return render(request, 'editar_alumno.html', {'ge':ge, 'des':des, 'sexo':sexo, 
			'cholu':cholu, 'valle':valle, 'alumno':alumno})
	else:
		return render(request, '404.html')

@login_required()
def editar_alumno_add(request):
	if request.user.is_staff:
		if request.method == 'POST':
			try:
				pk = request.POST.get('id')
				numid = request.POST.get('numid')
				nombre = request.POST.get('nombre')
				apellido = request.POST.get('apellido')
				direccion = request.POST.get('direccion')
				muni = request.POST.get('muni')
				ge = request.POST.get('ge')
				tel = request.POST.get('telefono')
				fechan = request.POST.get('fechan')
				edad = request.POST.get('edad')
				trabaja = request.POST.get('trabaja')
				ocupacion = request.POST.get('ocupacion')
				sex =  request.POST.get('sexo')
				
				mu = Municipio.objects.get(pk = muni)
				grupoe = GrupoEtnico.objects.get(pk = ge)
				des = Descicion.objects.get(pk = trabaja)
				sexo = Sexo.objects.get(pk = sex)

				alumno = Alumno.objects.get(pk = pk)
				alumno.numid = numid
				alumno.nombre = nombre
				alumno.apellido = apellido
				alumno.municipio = mu
				alumno.domicilio = direccion
				alumno.telefono = tel
				alumno.sexo = sexo
				alumno.grupo_etnico = grupoe
				alumno.trabaja = des
				alumno.ocupacion = ocupacion
				alumno.fecha_nacimiento = fechan
				alumno.edad = edad
				alumno.save()
				return HttpResponseRedirect(reverse('editar_alumno', args = [alumno.id]))
			except Exception as e:
				return HttpResponse(e)
	else:
		return render(request, '404.html')

@login_required()
def delete_alumno(request, pk):
	if request.user.is_staff:
		alumno = Alumno.objects.get(pk = pk)
		try:
			alumno.delete()
			return HttpResponseRedirect(reverse('alumnossinmat'))
		except Exception, e:
			return HttpResponse(e)
	else:
		return render(request, '404.html')

# FAMILIARES DEL ALUMNO X

@login_required()
def familiarxalumno(request, pk):
	if request.user.is_staff:
		alumno = Alumno.objects.get(pk = pk)
		familiar  = Familiar.objects.filter(familiar  = alumno)
		numu = familiar.count()
		return render(request, 'familiar.html', {'data':familiar, 'alumno':alumno, 'numu':numu})
	else:
		return render(request, '404.html')

@login_required()
def nuevo_familiar(request, pk):
	if request.user.is_staff:
		sexo = Sexo.objects.all()
		cholu = Municipio.objects.filter(depto = 1)
		valle = Municipio.objects.filter(depto = 2)
		des = Descicion.objects.all()
		parentezco = Parentezco.objects.all()
		alumno = Alumno.objects.get(pk = pk)
		return render(request, 'nuevo_familiar.html', {'des':des, 
			'sexo':sexo, 'cholu':cholu, 'valle':valle, 'parentezco': parentezco, 'alumno':alumno})
	else:
		return render(request, '404.html')

@login_required()
def familiar_add(request):
	if request.user.is_staff:
		if request.method == 'POST':
			try:
				numid = request.POST.get('numid')
				nombre = request.POST.get('nombre')
				apellido = request.POST.get('apellido')
				direccion = request.POST.get('direccion')
				muni = request.POST.get('muni')
				mu = Municipio.objects.get(pk = muni)
				tel = request.POST.get('telefono')
				fechan = request.POST.get('fechan')
				edad = request.POST.get('edad')
				trabaja = request.POST.get('trabaja')
				ocupacion = request.POST.get('ocupacion')
				sex =  request.POST.get('sexo')
				familiar =  request.POST.get('alumno')
				parentezco =  request.POST.get('parentezco')
				
				des = Descicion.objects.get(pk = trabaja)
				sexo = Sexo.objects.get(pk = sex)
				alumno = Alumno.objects.get(pk = familiar)
				pare = Parentezco.objects.get(pk = parentezco)

				persona = Familiar(
						numid = numid, 
						nombre = nombre,
						apellido = apellido,
						municipio = mu,
						domicilio = direccion,
						telefono = tel,
						sexo = sexo,
						trabaja = des,
						ocupacion = ocupacion,
						fecha_nacimiento = fechan,
						edad = edad,
						familiar = alumno,
						parentezco = pare)
				persona.save()
				return HttpResponseRedirect('/administrador/alumnos/')
			except Exception as e:
				return HttpResponse(e)
	else:
		return render(request, '404.html')

@login_required()
def editar_familiar(request, pk):
	if request.user.is_staff:
		sexo = Sexo.objects.all()
		cholu = Municipio.objects.filter(depto = 1)
		valle = Municipio.objects.filter(depto = 2)
		des = Descicion.objects.all()
		parentezco = Parentezco.objects.all()
		familiar = Familiar.objects.get(pk = pk)
		return render(request, 'editar_familiar.html', {'des':des, 
			'sexo':sexo, 'cholu':cholu, 'valle':valle, 'parentezco': parentezco, 'familiar':familiar})
	else:
		return render(request, '404.html')

@login_required()
def editar_familiar_add(request):
	if request.user.is_staff:
		if request.method == 'POST':
			try:
				pk = request.POST.get('id')
				numid = request.POST.get('numid')
				nombre = request.POST.get('nombre')
				apellido = request.POST.get('apellido')
				direccion = request.POST.get('direccion')
				muni = request.POST.get('muni')
				mu = Municipio.objects.get(pk = muni)
				tel = request.POST.get('telefono')
				fechan = request.POST.get('fechan')
				edad = request.POST.get('edad')
				trabaja = request.POST.get('trabaja')
				ocupacion = request.POST.get('ocupacion')
				sex =  request.POST.get('sexo')
				familiar =  request.POST.get('alumno')
				parentezco =  request.POST.get('parentezco')
				
				des = Descicion.objects.get(pk = trabaja)
				sexo = Sexo.objects.get(pk = sex)
				pare = Parentezco.objects.get(pk = parentezco)

				familiar = Familiar.objects.get(pk = pk)	
				familiar.numid = numid 
				familiar.nombre = nombre
				familiar.apellido = apellido
				familiar.municipio = mu
				familiar.domicilio = direccion
				familiar.telefono = tel
				familiar.sexo = sexo
				familiar.trabaja = des
				familiar.ocupacion = ocupacion
				familiar.fecha_nacimiento = fechan
				familiar.edad = edad
				familiar.parentezco = pare
				familiar.save()
				return HttpResponseRedirect(reverse('familiarxalumno', args = [familiar.familiar.id]))
			except Exception as e:
				return HttpResponse(e)
	else:
		return render(request, '404.html')

@login_required()
def delete_familiar(request, pk):
	if request.user.is_staff:
		familiar = Familiar.objects.get(pk = pk)
		try:
			familiar.delete()
			return HttpResponseRedirect(reverse('familiarxalumno', args = [familiar.familiar.id]))
		except Exception, e:
			return HttpResponse(e)
	else:
		return render(request, '404.html')

@login_required()
def alumnossinmat(request):
	if request.user.is_staff:
		alumno = Alumno.objects.all()
		matri = Matricula.objects.all().values_list('persona_id', flat=True)
		alumnos = alumno.exclude(id__in = matri)
		numu = alumnos.count()
		return render(request, 'alumnossinmat.html', {'data':alumnos, 'numu':numu})
	else:
		return render(request, '404.html')

# MATRICULA ALUMNO EN ESPECIFICO
@login_required()
def matricular_alumno(request, pk):
	if request.user.is_staff:
		alumno = Alumno.objects.get(pk = pk)
		grado = Grado.objects.all()
		centro = Centro.objects.all()
		periodo = Periodo.objects.all()
		des = Descicion.objects.all()
		ga = GradoAnterior.objects.all()
		config = Configuracion.objects.latest('id')
		fecha = config.periodo.fin_clases
		return render(request, 'matricular_alumno.html', {'des':des, 'alumno':alumno, 'grado': grado, 
			'centro':centro, 'periodo':periodo, 'ga':ga, 'config':config, 'fecha':fecha})
	else:
		return render(request, '404.html')

@login_required()
def matricular_alumno_add(request):
	if request.user.is_staff:
		if request.method == 'POST':
			try:
				alumno = request.POST.get('alumno')
				grado = request.POST.get('grado')
				centro = request.POST.get('centro')
				requisito = request.POST.get('requisito')
				gra = request.POST.get('ga')
				condicion = request.POST.get('condicion')
				otro = request.POST.get('otro')
				

				g = Grado.objects.get(pk=grado)
				c = Centro.objects.get(pk = centro)
				r = Descicion.objects.get(pk = requisito)
				a = Alumno.objects.get(pk = alumno)
				ga = GradoAnterior.objects.get(pk=gra)

				config = Configuracion.objects.latest('id')

				mat = Matricula(fecha = datetime.now() , persona = a, centro = c, grado = g, 
						num_periodo = config.periodo, requisito = r, grado_anterior = ga, condicion = condicion,
						otro = otro)	
				mat.save()
				return HttpResponseRedirect('/administrador/alumnos/')
			except Exception as e:
				return HttpResponse(e)
	else:
		return render(request, '404.html')

# FACILITADORES
@login_required()
def nuevo_faci(request, pk):
	if request.user.is_staff:
		sexo = Sexo.objects.all()
		cholu = Municipio.objects.filter(depto = 1)
		valle = Municipio.objects.filter(depto = 2)
		tipo_residencia = TipoResidencia.objects.all()
		des = Descicion.objects.all()
		fa = FormacionAcademica.objects.all()
		centro = Centro.objects.get(pk=pk)
		user = User.objects.all()
		faci = Facilitador.objects.all().values_list('usuario_id', flat=True)
		usuario = user.exclude(id__in = faci)
		return render(request, 'nuevo_facilitador.html', {'sexo':sexo, 'des':des, 'centro':centro, 
			'cholu':cholu, 'valle':valle, 'tipor':tipo_residencia, 'fa':fa, 'user':usuario})
	else:
		return render(request, '404.html')

@login_required()
def nuevo_faci_add(request):
	if request.user.is_staff:
		if request.method == 'POST':
			try:
				numid = request.POST.get('numid')
				nombre = request.POST.get('nombre')
				apellido = request.POST.get('apellido')
				tel = request.POST.get('telefono')
				direccion = request.POST.get('direccion')
				muni = request.POST.get('muni')
				opcio = request.POST.get('opcio')
				sex =  request.POST.get('sexo')
				ocupacion = request.POST.get('ocupacion')
				lugart = request.POST.get('lugart')
				formacion = request.POST.get('formacion')
				fechan = request.POST.get('fechan')
				edad = request.POST.get('edad')
				fechaf = request.POST.get('fechaf')
				becado = request.POST.get('becado')
				estudia = request.POST.get('estudia')
				dondee = request.POST.get('dondee')
				quee = request.POST.get('quee')
				otro = request.POST.get('otra_formacion')
				cent = request.POST.get('centro')
				# USUARIO
				username = request.POST.get('username')
				contra = request.POST.get('pass')
				correo = request.POST.get('correo')

				mu = Municipio.objects.get(pk = muni)
				tipor = TipoResidencia.objects.get(pk=opcio)
				sexo = Sexo.objects.get(pk = sex)
				be = Descicion.objects.get(pk = becado)
				es = Descicion.objects.get(pk = estudia)
				fa = FormacionAcademica.objects.get(pk = formacion)
				centro = Centro.objects.get(pk = cent)

				us = User.objects.create(
						username = username, 
						password = contra, 
						first_name = nombre, 
						last_name = apellido,
						email = correo
					)

				facilitador = Facilitador(
						numid = numid, 
						nombre = nombre,
						apellido = apellido,
						municipio = mu,
						tipo_residencia = tipor,
						domicilio = direccion,
						telefono = tel,
						sexo = sexo,
						ocupacion = ocupacion,
						lugar_trabajo = lugart,
						formacion_academica = fa,
						otra_formacion = otro,
						fecha_nacimiento = fechan,
						edad = edad,
						fecha_llenado = datetime.now(),
						tiempo_facilitador = fechaf,
						becado = be,
						estudia = es,
						donde_estudia = dondee,
						que_estudia = quee,
						centro = centro,
						usuario = us)
				facilitador.save()
				return HttpResponseRedirect(reverse('nuevo_faci', args=[centro.id]))
			except Exception as e:
				return HttpResponse(e)
	else:
		return render(request, '404.html')

@login_required()
def editar_faci(request, pk, pk2):
	if request.user.is_staff:
		sexo = Sexo.objects.all()
		cholu = Municipio.objects.filter(depto = 1)
		valle = Municipio.objects.filter(depto = 2)
		tipo_residencia = TipoResidencia.objects.all()
		des = Descicion.objects.all()
		fa = FormacionAcademica.objects.all()
		faci = Facilitador.objects.get(pk = pk)
		centro = Centro.objects.get(pk=pk2)
		return render(request, 'editar_facilitador.html', {'sexo':sexo, 'des':des, 'centro':centro, 
			'cholu':cholu, 'valle':valle, 'tipor':tipo_residencia, 'fa':fa, 'faci':faci})
	else:
		return render(request, '404.html')

@login_required()
def editar_faci_add(request):
	if request.user.is_staff:
		if request.method == 'POST':
			try:
				pk = request.POST.get('id')
				numid = request.POST.get('numid')
				nombre = request.POST.get('nombre')
				apellido = request.POST.get('apellido')
				tel = request.POST.get('telefono')
				direccion = request.POST.get('direccion')
				muni = request.POST.get('muni')
				opcio = request.POST.get('opcio')
				sex =  request.POST.get('sexo')
				ocupacion = request.POST.get('ocupacion')
				lugart = request.POST.get('lugart')
				formacion = request.POST.get('formacion')
				fechan = request.POST.get('fechan')
				edad = request.POST.get('edad')
				fechaf = request.POST.get('fechaf')
				becado = request.POST.get('becado')
				estudia = request.POST.get('estudia')
				dondee = request.POST.get('dondee')
				quee = request.POST.get('quee')
				otro = request.POST.get('otro')
				cent = request.POST.get('centro')
				

				mu = Municipio.objects.get(pk = muni)
				tipor = TipoResidencia.objects.get(pk=opcio)
				sexo = Sexo.objects.get(pk = sex)
				be = Descicion.objects.get(pk = becado)
				es = Descicion.objects.get(pk = estudia)
				fa = FormacionAcademica.objects.get(pk = formacion)
				centro = Centro.objects.get(pk = cent)

				facilitador = Facilitador.objects.get(pk = pk)
				facilitador.numid = numid 
				facilitador.nombre = nombre
				facilitador.apellido = apellido
				facilitador.municipio = mu
				facilitador.tipo_residencia = tipor
				facilitador.domicilio = direccion
				facilitador.telefono = tel
				facilitador.sexo = sexo
				facilitador.ocupacion = ocupacion
				facilitador.lugar_trabajo = lugart
				facilitador.formacion_academica = fa
				facilitador.otra_formacion = otro
				facilitador.fecha_nacimiento = fechan
				facilitador.edad = edad
				facilitador.tiempo_facilitador = fechaf
				facilitador.becado = be
				facilitador.estudia = es
				facilitador.donde_estudia = dondee
				facilitador.que_estudia = quee
				facilitador.centro = centro
				facilitador.save()
				return HttpResponseRedirect(reverse('facilitadorxcentro', args=[centro.id]))
			except Exception as e:
				return HttpResponse(e)
	else:
		return render(request, '404.html')

@login_required()
def delete_faci(request, pk, pk2):
	if request.user.is_staff:
		faci = Facilitador.objects.get(pk = pk)
		centro = Centro.objects.get(pk = pk2)
		try:
			faci.delete()
			return HttpResponseRedirect(reverse('facilitadorxcentro', args = [centro.id]))
		except Exception, e:
			return HttpResponse(e)
	else:
		return render(request, '404.html')

# MATRICULA MASIVA
@login_required()
def matricular(request, pk):
	if request.user.is_staff:
		alumno = Alumno.objects.all()
		centro = Centro.objects.get(pk = pk)
		grado = Grado.objects.filter(centro = centro)
		mat = Matricula.objects.all()
		matri = Matricula.objects.all().values_list('persona_id', flat=True)
		alumnos = alumno.exclude(id__in = matri)
		periodo = Periodo.objects.all()
		des = Descicion.objects.all()
		ga = GradoAnterior.objects.all()
		config = Configuracion.objects.latest('id')
		return render(request, 'matricular.html', {'des':des, 'alumnos':alumnos, 'grado': grado, 
			'centro':centro, 'mat':mat, 'periodo':periodo, 'ga':ga, 'config':config})
	else:
		return render(request, '404.html')


@login_required()
def matricular_add(request):
	if request.user.is_staff:
		if request.method == 'POST':
			try:
				alumnos = request.POST.getlist('alumno[]')
				grado = request.POST.get('grado')
				centro = request.POST.get('centro')
				requisito = request.POST.get('requisito')
				gra = request.POST.get('ga')
				condicion = request.POST.get('condicion')
				otro = request.POST.get('otro')

				g = Grado.objects.get(pk=grado)
				c = Centro.objects.get(pk = centro)
				config = Configuracion.objects.latest('id')
				r = Descicion.objects.get(pk = requisito)
				ga = GradoAnterior.objects.get(pk=gra)
				for alumno in alumnos:	
					a = Alumno.objects.get(pk=alumno)
					mat = Matricula(fecha = datetime.now() , persona = a, centro = c, grado = g, 
						num_periodo = config.periodo, requisito = r, grado_anterior = ga, condicion = condicion,
						otro = otro)	
					mat.save()
				return HttpResponseRedirect(reverse('matricular', args=[c.id]))
			except Exception as e:
				return HttpResponse(e)
	else:
		return render(request, '404.html')

@login_required()
def nuevo_grado(request, pk, pk2):
	if request.user.is_staff:
		faci = Facilitador.objects.get(pk = pk)
		centro = Centro.objects.get(pk = pk2)
		return render(request, 'nuevo_grado.html', {'faci':faci, 'centro': centro})
	else:
		return render(request, '404.html')

@login_required()
def nuevo_grado_add(request):
	if request.user.is_staff:
		if request.method == 'POST':
			try:
				grado = request.POST.get('grado')
				faci = request.POST.get('faci')
				cent = request.POST.get('centro')
				
				fa = Facilitador.objects.get(pk = faci)
				centro = Centro.objects.get(pk = cent)

				grado = Grado(
						grado = grado,
						facilitador = fa,
						centro = centro)
				grado.save()
				return HttpResponseRedirect(reverse('gradosxfacilitador', args=[fa.id, centro.id]))
			except Exception as e:
				return HttpResponse(e)
	else:
		return render(request, '404.html')

@login_required()
def delete_grado(request, pk):
	if request.user.is_staff:
		grado = Grado.objects.get(pk = pk)
		try:
			grado.delete()
			return HttpResponseRedirect('/principal/grados/')
		except Exception, e:
			return HttpResponse(e)
	else:
		return render(request, '404.html')


@login_required()
def certificados(request):
	if request.user.is_staff:
		return render(request, 'certificados.html')
	else:
		return render(request, '404.html')

@login_required()
def certificados_estudio(request):
	if request.user.is_staff:
		alumnos = Matricula.objects.all()
		return render(request, 'certificados_estudio.html', {'alumnos':alumnos})
	else:
		return render(request, '404.html')

@login_required()
def certificados_conducta(request):
	if request.user.is_staff:
		return render(request, 'certificados_conducta.html')
	else:
		return render(request, '404.html')

@login_required()
def certificados_himno(request):
	if request.user.is_staff:
		return render(request, 'certificados_himno.html')
	else:
		return render(request, '404.html')

@login_required()
def graficos(request):
	if request.user.is_staff:
		persona = Alumno.objects.all()
		# Grafrico por sexo
		masculino = persona.filter(sexo = 1)
		femenino = persona.filter(sexo = 2)
		numm = masculino.count()
		numf = femenino.count()

		m = Matricula.objects.all()
		# Grafico por grado
		primer =3
		primero = 3
		# MATRICULA POR GRADO: SEGUNDO
		segu = Grado.objects.get(grado = "Segundo")
		segundo = m.filter(grado=segu).count()
		# MATRICULA POR GRADO: TERCERO
		terc = 3
		tercero = 3
		# MATRICULA POR GRADO: CUARTO
		cuar = Grado.objects.get(grado = "Cuarto")
		cuarto = m.filter(grado=cuar).count()
		# MATRICULA POR GRADO: QUINTO
		quin = Grado.objects.get(grado = "Quinto")
		quinto = m.filter(grado=quin).count()
		# MATRICULA POR GRADO: SEXTO
		sex = Grado.objects.get(grado = "Sexto")
		sexto = m.filter(grado=sex).count()
		# MATRICULA POR GRADO: SEPTIMO
		sep = 3
		septimo = 3
		# MATRICULA POR GRADO: OCTAVO
		octa = 3
		octavo = 3
		# MATRICULA POR GRADO: NOVENO
		nove = 3
		noveno = 3


		return render(request, 'graficos.html', {'nummf':numf, 'numm':numm,
			'primero':primero,'segundo':segundo,'tercero':tercero,'cuarto':cuarto,
		'quinto':quinto,'sexto':sexto,'septimo':septimo, 'octavo':octavo,
		'noveno':noveno})
	else:
		return render(request, '404.html')