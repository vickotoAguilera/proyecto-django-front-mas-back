from django import forms
from django.utils.text import slugify
from .models import Curso

# aca creo el formulario basado en el modelo Curso (ModelForm)
class CursoForm(forms.ModelForm):
    class Meta:
        # aca vinculo el formulario al modelo Curso
        model = Curso
        # aca elijo los campos que voy a permitir rellenar desde la web
        fields = ['titulo', 'descripcion', 'nivel', 'duracion_horas', 'precio', 'categoria', 'instructor']
        
        # aca defino las etiquetas para que se vean legibles en pantalla
        labels = {
            'titulo': 'Título del curso',
            'descripcion': 'Descripción detallada',
            'nivel': 'Nivel pedagógico',
            'duracion_horas': 'Duración total (horas)',
            'precio': 'Precio ($ CLP)',
            'categoria': 'Categoría temática',
            'instructor': 'Instructor asignado',
        }
        
        # aca le inyecto clases CSS y placeholders a los inputs para que se vean bien con mi diseno
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-input', 
                'placeholder': 'Ej: Master en Python y Django'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-textarea', 
                'rows': 4, 
                'placeholder': 'Explica brevemente de qué trata el curso...'
            }),
            'nivel': forms.Select(attrs={'class': 'form-select'}),
            'duracion_horas': forms.NumberInput(attrs={
                'class': 'form-input', 
                'min': 1, 
                'placeholder': 'Ej: 40'
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-input', 
                'min': 0, 
                'placeholder': 'Ej: 29990'
            }),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'instructor': forms.Select(attrs={'class': 'form-select'}),
        }

    # aca inicializo el formulario y dejo los selectores por defecto en espanol
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categoria'].empty_label = "-- Selecciona una categoría --"
        self.fields['instructor'].empty_label = "-- Selecciona un instructor --"
        # aca dejo la opcion vacia de nivel en espanol tambien
        self.fields['nivel'].choices = [('', '-- Selecciona un nivel --')] + [c for c in self.fields['nivel'].choices if c[0] != '']

    # aca valido en el servidor que el precio no pueda ser un numero negativo
    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio is not None and precio < 0:
            raise forms.ValidationError("El precio no puede ser un valor negativo.")
        return precio

    # aca valido en el servidor que la duracion sea de al menos 1 hora
    def clean_duracion_horas(self):
        duracion = self.cleaned_data.get('duracion_horas')
        if duracion is not None and duracion <= 0:
            raise forms.ValidationError("La duración debe ser mayor a 0 horas.")
        return duracion

    # aca creo el slug automatico a partir del titulo si se crea un curso nuevo
    def save(self, commit=True):
        instancia = super().save(commit=False)
        if not instancia.slug:
            slug_base = slugify(instancia.titulo)
            slug_candidato = slug_base
            contador = 1
            while Curso.objects.filter(slug=slug_candidato).exclude(pk=instancia.pk).exists():
                slug_candidato = f"{slug_base}-{contador}"
                contador += 1
            instancia.slug = slug_candidato

        if commit:
            instancia.save()
        return instancia

