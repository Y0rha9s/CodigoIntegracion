from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Author(models.Model):
    User =  models.OneToOneField(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username

class Category(models.Model):
    tittle =  models.CharField(max_length=20)
    
    def __str__(self):
        return self.tittle

class Post(models.Model):
    title =  models.CharField(max_length=50)
    overview =  models.TextField()
    titmestamp =  models.DateTimeField(auto_now_add=True)
    coment_count = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    
    def __str__(self):
        return self.title


class Region(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'region'

class Contact (models.Model):
    nombres =  models.CharField(max_length=120)
    apellidos = models.CharField(max_length=120)
    telefono = models.IntegerField()
    
    class Meta:
        managed = True
        db_table = 'contact'
        
class Producto(models.Model):
    nombre = models.CharField(max_length = 64)
    categoria =  models.CharField(max_length = 32)
    precio =  models.IntegerField()
    
    def __str__(self):
        return f'{self.nombre} -> {self.precio}'
    
class Indicador(models.Model):
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    unidad_medida = models.CharField(max_length=20)
    fecha = models.DateTimeField()
    valor = models.FloatField()

    def __str__(self):
        return self.nombre
