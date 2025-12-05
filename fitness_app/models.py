from django.db import models
from django.contrib.auth.models import User

class Entrenador(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    experiencia = models.IntegerField(help_text="Años de experiencia")
    curriculum = models.TextField()
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    foto = models.ImageField(upload_to='entrenadores/', null=True, blank=True)
    
    def __str__(self):
        return self.nombre

class Gimnasio(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.CharField(max_length=20)
    entrenadores = models.ManyToManyField(Entrenador, related_name='gimnasios')
    
    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='articulos/', null=True, blank=True)
    
    def __str__(self):
        return self.titulo

class Habito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    ejercicio_realizado = models.CharField(max_length=200)
    duracion_minutos = models.IntegerField()
    calorias_quemadas = models.IntegerField()
    notas = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.usuario.username} - {self.fecha}"