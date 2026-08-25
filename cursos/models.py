from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Instructor(models.Model):
    nombre= models.CharField(max_length=100)
    especialidad = models.CharField(max_length=150)
    email = models.EmailField()
    anios_experiencia = models.IntegerField()

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    NIVELES = [
        ("Básico", "Básico"),
        ("Intermedio", "Intermedio"),
        ("Avanzado", "Avanzado")    
    ]

    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    descripcion = models.TextField()
    nivel = models.CharField(max_length=20, choices=NIVELES)
    duracion_horas = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
