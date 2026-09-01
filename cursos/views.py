from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Categoria, Instructor, Curso


def index(request):
    # Obtener parámetros de búsqueda y filtro desde la URL (GET)
    busqueda = request.GET.get('q', '').strip()
    categoria_id = request.GET.get('categoria', '').strip()

    # Consulta base optimizada
    cursos = Curso.objects.select_related('categoria', 'instructor').all()

    # Filtrar por texto si el usuario buscó algo
    if busqueda:
        cursos = cursos.filter(
            Q(titulo__icontains=busqueda) | Q(descripcion__icontains=busqueda)
        )

    # Filtrar por categoría si se seleccionó una
    if categoria_id and categoria_id.isdigit():
        cursos = cursos.filter(categoria_id=int(categoria_id))

    # Estadísticas para el Hero
    total_cursos = Curso.objects.count()
    total_categorias = Categoria.objects.count()
    total_instructores = Instructor.objects.count()
    categorias = Categoria.objects.all()

    context = {
        'cursos': cursos,
        'categorias': categorias,
        'busqueda': busqueda,
        'categoria_seleccionada': int(categoria_id) if categoria_id.isdigit() else None,
        'total_cursos': total_cursos,
        'total_categorias': total_categorias,
        'total_instructores': total_instructores,
    }
    return render(request, 'index.html', context)


def detalle_curso(request, slug):
    # Obtener el curso por su slug o devolver error 404 si no existe
    curso = get_object_or_404(
        Curso.objects.select_related('categoria', 'instructor'),
        slug=slug
    )

    # Obtener hasta 3 cursos relacionados de la misma categoría (excluyendo el actual)
    relacionados = Curso.objects.filter(
        categoria=curso.categoria
    ).exclude(id=curso.id)[:3]

    context = {
        'curso': curso,
        'relacionados': relacionados,
    }
    return render(request, 'detalle.html', context)

