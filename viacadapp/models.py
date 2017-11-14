from django.db import models

class Registro(models.Model):
	nombrecompleto= models.CharField(max_length= 80)
	correo= models.EmailField(max_length= 100)
	contraseña= models.CharField(max_length=32)
	foto= models.FileField(upload_to='viacadapp/profilephoto')
	materia= models.CharField(max_length=250)
	cualidades= models.CharField(max_length= 250)
	costohora= models.IntegerField(default=0)

class Materias(models.Model):
  materia= models.CharField(max_length=34)
  class Meta:
    managed=False
    db_table = 'viacadapp_materias'

  def __str__(self):
    return self.materia

class Alumnos(models.Model):
	nombrecompletoal= models.CharField(max_length= 80)
	correoal= models.EmailField(max_length= 100)
	contraseñaal= models.CharField(max_length=32)

class Solicitud(models.Model):
	responsable= models.CharField(max_length=80)
	direccion=models.CharField(max_length=30)
	fecha=models.DateTimeField(auto_now_add=True)

class Votaciones(models.Model):
	nombreprofesor=models.CharField(max_length=80)
	votacion=models.DecimalField( max_digits=5, decimal_places=2)

		