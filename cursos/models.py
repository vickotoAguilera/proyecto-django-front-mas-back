from django.db import models

# aca defino la tabla de Categoria para clasificar los cursos
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)        # nombre de la categoria (ej: programacion)
    descripcion = models.TextField()                 # descripcion detallada de la categoria

    # aca defino como quiero que se muestre la categoria en texto (ej: en el admin)
    def __str__(self):
        return self.nombre


# aca defino la tabla de Instructor con sus datos personales y profesionales
class Instructor(models.Model):
    nombre = models.CharField(max_length=100)        # nombre completo del profesor o profesora
    especialidad = models.CharField(max_length=150)  # area en la que es experto
    email = models.EmailField()                      # correo de contacto (valida formato email)
    anios_experiencia = models.IntegerField()        # anios de experiencia en el area

    def __str__(self):
        return self.nombre


# aca defino la tabla principal de Curso con sus atributos y relaciones
class Curso(models.Model):
    # aca defino las opciones fijas para el nivel del curso (lo que guardo en BD vs lo que muestro)
    NIVELES = [
        ("Básico", "Básico"),
        ("Intermedio", "Intermedio"),
        ("Avanzado", "Avanzado")    
    ]

    titulo = models.CharField(max_length=200)        # titulo comercial del curso
    slug = models.SlugField(unique=True)             # URL amigable (ej: python-desde-cero)
    descripcion = models.TextField()                 # explicacion completa de que trata el curso
    nivel = models.CharField(max_length=20, choices=NIVELES) # nivel usando la lista de opciones
    duracion_horas = models.IntegerField()           # total de horas pedagogicas
    precio = models.DecimalField(max_digits=10, decimal_places=0) # valor en pesos chilenos

    # aca relaciono el curso con Categoria (clave foranea muchos a uno).
    # uso on_delete=models.CASCADE para que si borro una categoria, se eliminen sus cursos en cascada
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    # aca relaciono el curso con Instructor (clave foranea muchos a uno)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

