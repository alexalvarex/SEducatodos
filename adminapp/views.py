from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from .models import *
from django.db.models import Count
from datetime import datetime
from reportlab.pdfgen import canvas
from cStringIO import StringIO
from io import BytesIO
from django.conf import settings
from django.views.generic import View

from django.contrib.auth.models import User

# Create your views here.

@login_required()
def index(request):
	return render(request, 'index.html')
@login_required()
def all_students(request):
	perfil = Personas.objects.all()
	sexo = Sexo.objects.all()
	ge = GrupoEtnico.objects.all()
	municipio = Municipio.objects.all()
	tp = TipoPersona.objects.get(pk = 1)
	des = Descicion.objects.all()
	alumnos = Personas.objects.filter(tipo_persona = tp)
	numu = alumnos.count()
	return render(request, 'all_students.html', {'data':alumnos, 'des':des, 'ge':ge, 'numu':numu, 'sexo':sexo, 'muni':municipio})


@login_required()
def new_student(request):
	sexo = Sexo.objects.all()
	ge = GrupoEtnico.objects.all()
	municipio = Municipio.objects.all()
	des = Descicion.objects.all()
	return render(request, 'new_student.html', {'ge':ge, 'des':des, 'sexo':sexo, 'muni':municipio})


@login_required()
def new_student_add(request):
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
			trabaja = request.POST.get('trabaja')
			des = Descicion.objects.get(pk = trabaja)
			ocupacion = request.POST.get('ocupacion')
			sex =  request.POST.get('sexo')
			sexo = Sexo.objects.get(pk = sex)
			tp = TipoPersona.objects.get(pk = 1)

			persona = Personas(
					numid = numid, 
					nombre = nombre,
					apellido = apellido,
					municipio = mu,
					domicilio = direccion,
					telefono = tel,
					sexo = sexo,
					tipo_persona = tp,
					grupo_etnico = grupoe,
					trabaja = des,
					ocupacion = ocupacion,
					fecha_nacimiento = fechan)
			persona.save()
			return HttpResponseRedirect('/principal/alumnos/')
		except Exception as e:
			return HttpResponse(e)

@login_required()
def edit_students(request, pk):
		if request.method == 'POST':
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
			trabaja = request.POST.get('trabaja')
			des = Descicion.objects.get(pk = trabaja)
			ocupacion = request.POST.get('ocupacion')
			sexo =  request.POST.get('sexo')
			sex = Sexo.objects.get(pk = sexo)
			tp = TipoPersona.objects.get(pk = 1)

			P = Personas.objects.get(pk=pk)
			P.numid = numid
			P.nombre = nombre
			P.apellido = apellido
			P.domicilio = direccion
			P.telefono = tel
			P.municipio = mu
			P.grupo_etnico = grupoe
			P.fecha_nacimiento = fechan
			P.trabaja = des
			P.ocupacion = ocupacion
			P.sexo = sex
			P.tipo_persona = tp
			P.save()
		return HttpResponseRedirect('/principal/alumnos/')


@login_required()
def delete_student(request, pk):
	alumno = Personas.objects.get(pk = pk)
	try:
		alumno.delete()
		return HttpResponseRedirect('/principal/alumnos/')
	except Exception, e:
		return HttpResponse(e)

# PROMOTORES
@login_required()
def all_promotores(request):
	perfil = Personas.objects.all()
	sexo = Sexo.objects.all()
	ge = GrupoEtnico.objects.all()
	municipio = Municipio.objects.all()
	tp = TipoPersona.objects.get(pk = 2)
	des = Descicion.objects.all()
	promotor = Personas.objects.filter(tipo_persona = tp)
	numu = promotor.count()
	return render(request, 'all_promotores.html', {'data':promotor, 'des':des, 'ge':ge, 'numu':numu, 'sexo':sexo, 'muni':municipio})


@login_required()
def new_promotor(request):
	sexo = Sexo.objects.all()
	ge = GrupoEtnico.objects.all()
	municipio = Municipio.objects.all()
	des = Descicion.objects.all()
	return render(request, 'new_promotor.html', {'ge':ge, 'des':des, 'sexo':sexo, 'muni':municipio})


@login_required()
def new_promotor_add(request):
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
			trabaja = request.POST.get('trabaja')
			des = Descicion.objects.get(pk = trabaja)
			ocupacion = request.POST.get('ocupacion')
			sex =  request.POST.get('sexo')
			sexo = Sexo.objects.get(pk = sex)
			tp = TipoPersona.objects.get(pk = 2)

			persona = Personas(
					numid = numid, 
					nombre = nombre,
					apellido = apellido,
					municipio = mu,
					domicilio = direccion,
					telefono = tel,
					sexo = sexo,
					tipo_persona = tp,
					grupo_etnico = grupoe,
					trabaja = des,
					ocupacion = ocupacion,
					fecha_nacimiento = fechan)
			persona.save()
			return HttpResponseRedirect('/principal/promotores/')
		except Exception as e:
			return HttpResponse(e)

@login_required()
def edit_promotores(request, pk):
		if request.method == 'POST':
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
			trabaja = request.POST.get('trabaja')
			des = Descicion.objects.get(pk = trabaja)
			ocupacion = request.POST.get('ocupacion')
			sexo =  request.POST.get('sexo')
			sex = Sexo.objects.get(pk = sexo)
			tp = TipoPersona.objects.get(pk = 2)

			P = Personas.objects.get(pk=pk)
			P.numid = numid
			P.nombre = nombre
			P.apellido = apellido
			P.domicilio = direccion
			P.telefono = tel
			P.municipio = mu
			P.grupo_etnico = grupoe
			P.fecha_nacimiento = fechan
			P.trabaja = des
			P.ocupacion = ocupacion
			P.sexo = sex
			P.tipo_persona = tp
			P.save()
		return HttpResponseRedirect('/principal/promotores/')


@login_required()
def delete_promotor(request, pk):
	promotor = Personas.objects.get(pk = pk)
	try:
		promotor.delete()
		return HttpResponseRedirect('/principal/promotores/')
	except Exception, e:
		return HttpResponse(e)


# FACILITADORES

@login_required()
def all_facilitador(request):
	faci = Facilitador.objects.all()
	sexo = Sexo.objects.all()
	municipio = Municipio.objects.all()
	tipor = TipoResidencia.objects.all()
	des = Descicion.objects.all()
	numf = faci.count()
	return render(request, 'all_facilitador.html', {'data':faci, 'des':des, 'numu':numf, 'sexo':sexo, 'muni':municipio, 'tipor':tipor})

@login_required()
def new_facilitador(request):
	sexo = Sexo.objects.all()
	municipio = Municipio.objects.all()
	tipo_residencia = TipoResidencia.objects.all()
	des = Descicion.objects.all()
	return render(request, 'new_facilitador.html', {'sexo':sexo, 'des':des, 'muni':municipio, 'tipor':tipo_residencia})

@login_required()
def new_facilitador_add(request):
	if request.method == 'POST':
		try:
			numid = request.POST.get('numid')
			nombre = request.POST.get('nombre')
			apellido = request.POST.get('apellido')
			tel = request.POST.get('telefono')
			direccion = request.POST.get('direccion')
			muni = request.POST.get('muni')
			mu = Municipio.objects.get(pk = muni)
			opcio = request.POST.get('opcio')
			tipor = TipoResidencia.objects.get(pk=opcio)
			sex =  request.POST.get('sexo')
			sexo = Sexo.objects.get(pk = sex)
			correo = request.POST.get('correo')
			ocupacion = request.POST.get('ocupacion')
			lugart = request.POST.get('lugart')
			formacion = request.POST.get('formacion')
			fechan = request.POST.get('fechan')
			fechaf = request.POST.get('fechaf')
			becado = request.POST.get('becado')
			be = Descicion.objects.get(pk = becado)
			estudia = request.POST.get('estudia')
			es = Descicion.objects.get(pk = estudia)
			dondee = request.POST.get('dondee')
			quee = request.POST.get('quee')




			facilitador = Facilitador(
					numid = numid, 
					nombre = nombre,
					apellido = apellido,
					municipio = mu,
					tipo_residencia = tipor,
					domicilio = direccion,
					telefono = tel,
					sexo = sexo,
					correo = correo,
					ocupacion = ocupacion,
					lugar_trabajo = lugart,
					formacion_academica = formacion,
					fecha_nacimiento = fechan,
					fecha_llenado = datetime.now(),
					tiempo_facilitador = fechaf,
					becado = be,
					estudia = es,
					donde_estudia = dondee,
					que_estudia = quee)
			facilitador.save()
			return HttpResponseRedirect('/principal/facilitador/')
		except Exception as e:
			return HttpResponse(e)

@login_required()
def edit_facilitador(request, pk):
		if request.method == 'POST':
			numid = request.POST.get('numid')
			nombre = request.POST.get('nombre')
			apellido = request.POST.get('apellido')
			tel = request.POST.get('telefono')
			direccion = request.POST.get('direccion')
			muni = request.POST.get('muni')
			mu = Municipio.objects.get(pk = muni)
			opcio = request.POST.get('opcio')
			tipor = TipoResidencia.objects.get(pk=opcio)
			sex =  request.POST.get('sexo')
			sexo = Sexo.objects.get(pk = sex)
			correo = request.POST.get('correo')
			ocupacion = request.POST.get('ocupacion')
			lugart = request.POST.get('lugart')
			formacion = request.POST.get('formacion')
			fechan = request.POST.get('fechan')
			fechaf = request.POST.get('fechaf')
			becado = request.POST.get('becado')
			estudia = request.POST.get('estudia')
			dondee = request.POST.get('dondee')
			quee = request.POST.get('quee')

			F = Facilitador.objects.get(pk=pk)
			F.numid = numid, 
			F.nombre = nombre,
			F.apellido = apellido,
			F.municipio = mu,
			F.tipo_residencia = tipor,
			F.domicilio = direccion,
			F.telefono = tel,
			F.sexo = sexo,
			F.correo = correo,
			F.ocupacion = ocupacion,
			F.lugar_trabajo = lugart,
			F.formacion_academica = formacion,
			F.fecha_nacimiento = fechan,
			F.fecha_llenado = datetime.now(),
			F.tiempo_facilitador = fechaf,
			F.becado = valor,
			F.estudia = valor2,
			F.donde_estudia = dondee,
			F.que_estudia = quee
			F.save()
		return HttpResponseRedirect('/principal/facilitador/')

@login_required()
def delete_facilitador(request, pk):
	faci = Facilitador.objects.get(pk = pk)
	try:
		faci.delete()
		return HttpResponseRedirect('/principal/facilitador/')
	except Exception, e:
		return HttpResponse(e)

@login_required()
def all_grados(request):
	grado = Grado.objects.all()
	faci = Facilitador.objects.all()
	numf = grado.count()
	return render(request, 'all_grados.html', {'data':grado, 'faci':faci})

@login_required()
def new_grado(request):
	faci = Facilitador.objects.all()
	return render(request, 'new_grado.html', {'faci':faci})

@login_required()
def new_grado_add(request):
	if request.method == 'POST':
		try:
			grado = request.POST.get('grado')
			faci = request.POST.get('faci')
			fa = Facilitador.objects.get(pk = faci)

			grado = Grado(
					grado = grado,
					facilitador = fa)
			grado.save()
			return HttpResponseRedirect('/principal/grados/')
		except Exception as e:
			return HttpResponse(e)

@login_required()
def delete_grado(request, pk):
	grado = Grado.objects.get(pk = pk)
	try:
		grado.delete()
		return HttpResponseRedirect('/principal/grados/')
	except Exception, e:
		return HttpResponse(e)

@login_required()
def edit_grado(request, pk):
		if request.method == 'POST':
			grado = request.POST.get('grado')
			faci = request.POST.get('faci')
			fa = Facilitador.objects.get(pk = faci)

			F = Grado.objects.get(pk=pk)
			F.grado = grado
			F.facilitador = fa
			F.save()
		return HttpResponseRedirect('/principal/grados/')

@login_required()
def all_centros(request):
	centro = Centro.objects.all()
	tipoc = TipoCentro.objects.all()
	patro = Patrocinador.objects.all()
	zona = Zona.objects.all()
	des = Descicion.objects.all()
	tp = TipoPersona.objects.get(pk = 2)
	promotor = Personas.objects.filter(tipo_persona = tp)
	numf = centro.count()
	return render(request, 'all_centros.html', {'data':centro, 'des':des, 'tipoc':tipoc, 'patro':patro, 'zona':zona, 'promo': promotor})

@login_required()
def new_centro(request):
	tipoc = TipoCentro.objects.all()
	patro = Patrocinador.objects.all()
	zona = Zona.objects.all()
	des = Descicion.objects.all()
	tp = TipoPersona.objects.get(pk = 2)
	promotor = Personas.objects.filter(tipo_persona = tp)
	return render(request, 'new_centro.html', {'des':des,'tipoc':tipoc, 'patro':patro, 'zona':zona, 'promo': promotor})

@login_required()
def new_centro_add(request):
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
					promotor = prom,
					donde_funciona = donde,
					direccion = direccion)
			centro.save()
			return HttpResponseRedirect('/principal/centros/')
		except Exception as e:
			return HttpResponse(e)

@login_required()
def delete_centro(request, pk):
	centro = Centro.objects.get(pk = pk)
	try:
		centro.delete()
		return HttpResponseRedirect('/principal/centros/')
	except Exception, e:
		return HttpResponse(e)

@login_required()
def edit_centro(request, pk):
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
		return HttpResponseRedirect('/principal/centros/')

@login_required()
def new_enroll(request):
		tp = TipoPersona.objects.get(pk = 1)
		persona = Personas.objects.filter(tipo_persona = 1)
		centro = Centro.objects.all()
		grado = Grado.objects.all()
		mat = Matricula.objects.all()
		matri = Matricula.objects.filter(grado = grado).values_list('persona_id', flat=True)
		alumnos = persona.exclude(id__in = matri)
		periodo = Periodo.objects.all()
		des = Descicion.objects.all()
		return render(request, 'new_enroll.html', {'des':des, 'alumnos':alumnos, 'grado': grado, 
			'centro':centro, 'mat':mat, 'periodo':periodo})


@login_required()
def new_enroll_add(request):
	if request.method == 'POST':
		try:
			alumnos = request.POST.getlist('alumno[]')
			grado = request.POST.get('grado')
			centro = request.POST.get('centro')
			primer = request.POST.get('primer')
			horario = request.POST.get('horario')
			fechai = request.POST.get('fechai')
			fechaf = request.POST.get('fechaf')
			archivos = request.FILES['archivos']

			g = Grado.objects.get(pk=grado)
			c = Centro.objects.get(pk = centro)
			d = Periodo.objects.get(pk=primer)
			for alumno in alumnos:	
				a = Personas.objects.get(pk=alumno)
				mat = Matricula(fecha = datetime.now() , persona = a, centro = c, grado = g, 
					num_periodo = d, horario = horario, 
					inicio_clases = fechai, fin_clases = fechaf, requisito = archivos)	
				mat.save()
			return HttpResponseRedirect('/principal/enroll/new/')
		except Exception as e:
			return HttpResponse(e)

@login_required()
def enroll_massive(request):
	if request.user.Perfil.es_admin:
		ga = OfertaGrado.objects.all()
		configuracion = Configuracion.objects.get(pk=1)
		anio = configuracion.anioactual
		ofergra = OfertaGrado.objects.filter(anio = anio)
		ofergra2 = OfertaGrado.objects.exclude(anio = anio)
		return render(request, 'massive_enroll.html', {'ga':ga, 'ofergra':ofergra, 'ofergra2': ofergra2})
	else:
		return render(request, 'denegado.html')

@login_required()
def enroll_massive_add(request):
		if request.method == 'POST':
			try:
				gradoM = request.POST.get('gradom')
				gradoA = request.POST.get('gradoa')
				gradoAnterior = OfertaGrado.objects.get(pk=gradoA)
				alumnos = Matricula.objects.filter(ofertagrado = gradoAnterior)
				go = OfertaGrado.objects.get(pk=gradoM)
				gc = GradoClase.objects.filter(grado = go.gradoseccion.grado)
				for alumno in alumnos:	
					a = Alumno.objects.get(pk=alumno.alumno.id)
					go.cupos = go.cupos - 1
					mat = Matricula(alumno = a, ofertagrado = go)	
					mat.save()
					go.save()
					for gradoc in gc:
						ec = EstadoClase.objects.get(pk=1)
						of = OfertaClase.objects.get(ofertagrado = go, gradoclase = gradoc)
						dt = DetalleMatricula(ofertaclase = of, matricula = mat, estadoclase = ec)
						dt.save()
				return HttpResponseRedirect('/admini/enroll/massive/')
			except Exception as e:
				return HttpResponse(e)

@login_required()
def all_enroll(request):
	m = Matricula.objects.all()
	return render(request, 'all_enroll.html', {'m':m})

@login_required()
def view_matricula(request, ida):
	alu = Alumno.objects.get(pk = ida)
	matri = Matricula.objects.filter(alumno = alu)
	m = matri.count()
	# if matri.count() > 0:
	return render(request, 'enroll_student.html', {'matri': matri, 'm': m})

@login_required()
def all_reports(request):
	return render(request, 'all_reports.html')

@login_required()
def all_graphics(request):
	persona = Personas.objects.filter(tipo_persona = 1)
	# Grafrico por sexo
	masculino = persona.filter(sexo = 1)
	femenino = persona.filter(sexo = 2)
	numm = masculino.count()
	numf = femenino.count()
	# Grafico por grado
	primer = Grado.objects.get(grado = "Primero")
	mat1 = Matricula.objects.filter(grado = primer)
	primero = mat1.count()
	seg = Grado.objects.get(grado = "Segundo")
	mat2 = Matricula.objects.filter(grado = seg)
	segundo = mat2.count()
	tercer = Grado.objects.get(grado = "Tercero")
	mat3 = Matricula.objects.filter(grado = tercer)
	tercero = mat3.count()
	cuart = Grado.objects.get(grado = "Cuarto")
	mat4 = Matricula.objects.filter(grado = cuart)
	cuarto = mat4.count()
	quin = Grado.objects.get(grado = "Quinto")
	mat5 = Matricula.objects.filter(grado = quin)
	quinto = mat5.count()
	sex = Grado.objects.get(grado = "Sexto")
	mat6 = Matricula.objects.filter(grado = sex)
	sexto = mat6.count()
	sep = Grado.objects.get(grado = "Septimo")
	mat7 = Matricula.objects.filter(grado = sep)
	septimo = mat7.count()
	octa = Grado.objects.get(grado = "Octavo")
	mat8 = Matricula.objects.filter(grado = octa)
	octavo = mat8.count()
	nov = Grado.objects.get(grado = "Noveno")
	mat9 = Matricula.objects.filter(grado = nov)
	noveno = mat9.count()
	# Grafico por centro
	centro = Centro.objects.all()
	matriculas = Matricula.objects.filter()


	return render(request, 'all_graphics.html', {'nummf':numf, 'numm':numm,
		'primero':primero,'segundo':segundo,'tercero':tercero,'cuarto':cuarto,
		'quinto':quinto,'sexto':sexto,'septimo':septimo, 'octavo':octavo,
		'noveno':noveno})


@login_required()
def reportes(request):
	# ALUMNOS
	personas = Personas.objects.all()
	sexo = Sexo.objects.all()
	ge = GrupoEtnico.objects.all()
	municipio = Municipio.objects.all()
	tp = TipoPersona.objects.get(pk = 1)
	tpromo = TipoPersona.objects.get(pk = 2)
	des = Descicion.objects.all()
	alumnos = Personas.objects.filter(tipo_persona = tp)
	year = datetime.now()
	numu = alumnos.count()
	m = Matricula.objects.all()
	# MATRICULA POR GRADO: PRIMERO
	primer = Grado.objects.get(grado = "Primero")
	primero = m.filter(grado=primer)
	# MATRICULA POR GRADO: SEGUNDO
	segu = Grado.objects.get(grado = "Segundo")
	segundo = m.filter(grado=segu)
	# MATRICULA POR GRADO: TERCERO
	terc = Grado.objects.get(grado = "Tercero")
	tercero = m.filter(grado=terc)
	# MATRICULA POR GRADO: CUARTO
	cuar = Grado.objects.get(grado = "Cuarto")
	cuarto = m.filter(grado=cuar)
	# MATRICULA POR GRADO: QUINTO
	quin = Grado.objects.get(grado = "Quinto")
	quinto = m.filter(grado=quin)
	# MATRICULA POR GRADO: SEXTO
	sex = Grado.objects.get(grado = "Sexto")
	sexto = m.filter(grado=sex)
	# MATRICULA POR GRADO: SEPTIMO
	sep = Grado.objects.get(grado = "Septimo")
	septimo = m.filter(grado=sep)
	# MATRICULA POR GRADO: OCTAVO
	octa = Grado.objects.get(grado = "Octavo")
	octavo = m.filter(grado=octa)
	# MATRICULA POR GRADO: NOVENO
	nove = Grado.objects.get(grado = "Noveno")
	noveno = m.filter(grado=nove)
	# PROMOTORES
	promotor = Personas.objects.filter(tipo_persona = tpromo)
	# Facilitadores
	faci = Facilitador.objects.all()
	sexo = Sexo.objects.all()
	municipio = Municipio.objects.all()
	tipor = TipoResidencia.objects.all()
	des = Descicion.objects.all()
	numf = faci.count()
	# grados
	grado = Grado.objects.all()
	faci = Facilitador.objects.all()
	numf = grado.count()
	# centros
	centro = Centro.objects.all()
	tipoc = TipoCentro.objects.all()
	patro = Patrocinador.objects.all()
	zona = Zona.objects.all()
	des = Descicion.objects.all()
	tp = TipoPersona.objects.get(pk = 2)


	return render(request, 'reportes_fisico.html', {'grado':grado,'faci':faci,'m':primero, 'data':alumnos, 
		'des':des, 'ge':ge, 'numu':numu, 'sexo':sexo, 'muni':municipio, 'year':year,
		'centro':centro, 'des':des, 'tipoc':tipoc, 'patro':patro, 'zona':zona, 'promo': promotor,
		'segundo':segundo,'tercero':tercero,'cuarto':cuarto,
		'quinto':quinto,'sexto':sexto,'septimo':septimo, 'octavo':octavo,
		'noveno':noveno})
