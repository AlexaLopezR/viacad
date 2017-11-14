
from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^$',views.index,name='index'),
   url(r'^registroProfesores/$', views.registroProfesores,name='registroProfesores' ),
   url(r'^registroAlumnos/$', views.registroAlumnos,name='registroAlumnos' ),
   url(r'^registroAlumnos/buscarprof/$', views.buscarprof,name='buscarprof' ),
   url(r'^elegido/buscarprof/$', views.buscarprof,name='buscarprof' ),
   url(r'^elegido/$', views.registroSolicitud,name='elegido' )
]