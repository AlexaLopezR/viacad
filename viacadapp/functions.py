import json 
from .models import Materias
#run once
def CrearMaterias():
	ListaMaterias=['Matematicas', 'Español', 'Biología',
			'Sociales', 'Geometría', 'Programación',
			'Contabilidad', 'Estadística', 'Idiomas', 
			'Física', 'Química', 'Música' ]
	for i in range (0, len(ListaMaterias)):
		M=Materias(id=i+1, materia=ListaMaterias[i])
		M.save()

def ListaMaterias():
	choices= list(Materias.objects.values_list('materia', flat=True))
	for i in range(0,len(choices)):
		choices[i]=(choices[i],choices[i])
	return choices

def ListaProfesores():
	choices= list(Materias.objects.values_list('materia', flat=True))
