from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Categoria, Instructor, Curso


# -------------------------------------------------------------
# vista 1: catalogo principal con buscador y filtros
# -------------------------------------------------------------
def index(request):
    # aca capturo lo que el usuario escribio en el buscador (GET con parametro 'q')
    busqueda = request.GET.get('q', '').strip()

    # aca capturo la categoria que el usuario pincho en los botones de filtro (GET con parametro 'categoria')
    categoria_id = request.GET.get('categoria', '').strip()

    # aca hago la consulta base a la base de datos:
    # traigo todos los cursos y uso select_related para traer de una sola vez Categoria e Instructor
    # asi optimizo la consulta y evito hacer multiples viajes a la base de datos (problema N+1)
    cursos = Curso.objects.select_related('categoria', 'instructor').all()

    # si el usuario escribio un texto en el buscador, aca filtro:
    # con Q busco si el texto coincide con el titulo o con la descripcion (icontains = sin distinguir mayusculas)
    if busqueda:
        cursos = cursos.filter(
            Q(titulo__icontains=busqueda) | Q(descripcion__icontains=busqueda)
        )

    # si el usuario selecciono una categoria valida, aca filtro los cursos por esa categoria
    if categoria_id and categoria_id.isdigit():
        cursos = cursos.filter(categoria_id=int(categoria_id))

    # aca calculo las estadisticas generales para mostrarlas en los contadores del Hero
    total_cursos = Curso.objects.count()
    total_categorias = Categoria.objects.count()
    total_instructores = Instructor.objects.count()
    categorias = Categoria.objects.all()

    # aca empaqueto todas las variables en un diccionario llamado 'context'
    # este diccionario es el que le envio al template HTML para que pueda dibujar los datos
    context = {
        'cursos': cursos,
        'categorias': categorias,
        'busqueda': busqueda,
        'categoria_seleccionada': int(categoria_id) if categoria_id.isdigit() else None,
        'total_cursos': total_cursos,
        'total_categorias': total_categorias,
        'total_instructores': total_instructores,
    }

    # aca renderizo la plantilla 'index.html' pasandole el request y el contexto con mis datos
    return render(request, 'index.html', context)


# -------------------------------------------------------------
# vista 2: ficha de detalle de un curso individual
# -------------------------------------------------------------
def detalle_curso(request, slug):
    # aca busco el curso especifico usando su slug (la parte bonita de la URL, ej: python-desde-cero)
    # uso get_object_or_404: si el curso existe me lo entrega, pero si no existe arroja automaticamente un error 404
    curso = get_object_or_404(
        Curso.objects.select_related('categoria', 'instructor'),
        slug=slug
    )

    # aca busco hasta 3 cursos relacionados que pertenezcan a la misma categoria,
    # excluyendo el curso actual (.exclude(id=curso.id)) para no recomendar el mismo que ya esta viendo
    relacionados = Curso.objects.filter(
        categoria=curso.categoria
    ).exclude(id=curso.id)[:3]

    # aca armo el contexto con el curso encontrado y su lista de relacionados
    context = {
        'curso': curso,
        'relacionados': relacionados,
    }

    # aca le mando los datos a la plantilla 'detalle.html'
    return render(request, 'detalle.html', context)



