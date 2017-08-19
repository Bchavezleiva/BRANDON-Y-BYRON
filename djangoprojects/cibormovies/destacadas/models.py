from django.db import models

# Create your models here.
class author(models.Model):
    name=models.CharField(max_length=50,help_text='Ingrese el nombre del autor: ')
    surname=models.CharField(max_length=50,help_text='Ingrese el apellido del author: ')
    bday=models.DateField(help_text='Selecciona la fecha de nacimiento: ')
    genere=models.CharField(max_length=50,help_text='Ingrese su genero: ')
    email=models.EmailField(help_text='Ingrese su e-mail: ')

class post(models.Model):
    title=models.CharField(max_length=50,help_text='Titulo de la pelicula: ')
    company=models.CharField(max_length=50,help_text='Nombre de la compañia productora: ')
    pubdate=models.DateField(help_text='Fecha de pelicula: ')
    director=models.CharField(max_length=50,help_text='Director de la pelicula: ')
    category=models.CharField(max_length=50,help_text='Categorias de la pelicula: ')
    sipnosis=models.CharField(max_length=50,help_text='Sipnosis de la pelicula: ')
    review=models.CharField(max_length=500,help_text='Opinion de la cinta: ')
    stars=models.DecimalField(decimal_places=2, max_digits=10, help_text='Puntuacion que le damos: ')
