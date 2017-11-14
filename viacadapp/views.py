from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse  
from django.core.files.storage import FileSystemStorage
from django.conf import settings 
from django.contrib import messages
from django.core.mail import send_mail
from django.core import mail
from django.core.mail import EmailMessage
import smtplib
import datetime
from smtplib import SMTPException


from .functions import CrearMaterias 
from .forms import FormularioInscripcionProfesores 
from .forms import FormularioInscripcionAlumnos 
from .forms import ElegirMateria 
from .forms import FormularioSolicitud 

from .models import Registro
from .models import Alumnos
from .models import Materias
from .models import Solicitud


# Create your views here.
def index(request):
	try:
		if (request.session['registrado']==1):
			temp=request.session['registrado']
			del request.session['registrado']
			return render(request,'viacadapp/index.html',{'message':temp})
	except:
		return render(request,'viacadapp/index.html')

def registroProfesores(request):
	#CrearMaterias()
	#generate form
	if request.method=='POST':
		form=FormularioInscripcionProfesores(request.POST, request.FILES)
		registrado=0
		if form.is_valid():
			nc=form.cleaned_data['nombrecompleto']
			correo= form.cleaned_data['correo']
			contra= form.cleaned_data['contraseña']
			foto= request.FILES['foto']
			mat= form.cleaned_data['materia']
			cuali=form.cleaned_data['cualidades']
			hora=form.cleaned_data['costohora']
			g=Registro(nombrecompleto=nc, correo=correo, contraseña=contra, foto=foto,
			 			materia=mat, cualidades=cuali, costohora=hora)
			g.save()
			registrado=1
			request.session['registrado']=registrado
			return redirect("/")
	else:
		form=FormularioInscripcionProfesores()
		return render(request, 'viacadapp/registroProfesores.html',{'form':form})


def registroAlumnos(request):
	if request.method=='POST':
		form=FormularioInscripcionAlumnos(request.POST, request.FILES)
		registrado=0
		if form.is_valid():
			nc=form.cleaned_data['nombrecompletoal']
			correo= form.cleaned_data['correoal']
			contra= form.cleaned_data['contraseñaal']
			request.session['correo'] = correo #Enviar correo a otra view
			g=Alumnos(nombrecompletoal=nc, correoal=correo, contraseñaal=contra)
			g.save()
			registrado=1
			request.session['registrado']=registrado

			return redirect("buscarprof/")

	else:
		form=FormularioInscripcionAlumnos()
		return render(request, 'viacadapp/registroAlumnos.html',{'form':form})
	

def buscarprof(request):
	if request.method=='POST':
		form=ElegirMateria(request.POST)

		if form.is_valid():
			sheet=form.cleaned_data['category']	
			request.session['sheet']=sheet #Materia seleccionada
			return redirect("/elegido")

	else:
		form=ElegirMateria()
		return render(request, 'viacadapp/buscarprof.html',{'form':form})

def registroSolicitud(request):
	if request.method=='POST':
		form=FormularioSolicitud(request.POST, request.FILES)
		if form.is_valid():
			resp=form.cleaned_data['responsable']
			casa= form.cleaned_data['direccion']
			fecha= form.cleaned_data['fecha']
			correo = request.session.get('correo')
			print(correo)
			g=Solicitud(responsable=resp, direccion=casa, fecha=fecha)
			g.save()
			smtp=smtplib.SMTP('smtp.gmail.com')
			smtp.ehlo()
			smtp.starttls()
			smtp.ehlo()
			smtp.login('alexacaro14', 'cosafa2008')
			FROM= 'alexacaro14'
			TO= correo
			formato = "%m-%d-%Y"
			dia  = fecha.strftime(formato)
			asunto= 'Confirmacion de solicitud'
			mensaje= 'Ha solicitado una tutoria a nombre de ' + resp+ ' , la cual se llevara a cabo en la '+ casa + ' el dia ' + dia+ '. Gracias por elegirnos'
			texto = message = """From: %s\nTo: %s\nSubject: %s\n\n%s
			""" % (FROM, ", ".join(TO), asunto, mensaje) 
			smtp.sendmail(FROM, correo, texto)
			return redirect("buscarprof/")
			
	else:
		form=FormularioSolicitud()
		return render(request, 'viacadapp/elegido.html',{'form':form})

