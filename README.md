# Directorio de Cursos — Proyecto Django (Evaluación 1)

Bienvenidos a mi proyecto del módulo **"Desarrollo de aplicaciones del lado del servidor"**. Es un **Directorio de Cursos** que nace con datos en JSON (eval 1) y que está pensado para convertirse en una app (eval 2) y en una API con Django REST Framework (eval 3), manteniendo los mismos modelos y la misma base de datos.

Este README es mi **diario de trabajo**: lo voy actualizando en cada push con los pasos que voy completando.

---

## Semana 1 — Arranque del proyecto

### Qué hice con la ayuda de la IA (deepseek v4 flash)

Le pedí a la IA que me creara el **frontend completo** (HTML, CSS y JavaScript) mientras yo comenzaba con el backend de Django paso a paso, siguiendo la división de roles que nos indicó el profesor: el agente de IA hace el front y yo escribo el backend.

**El frontend quedó así (carpeta `front/`):**
- `index.html` — página principal con hero, buscador, filtros por categoría y grilla de tarjetas de cursos.
- `detalle.html` — ficha de cada curso con su instructor y cursos relacionados.
- `css/style.css` — estilo verde esmeralda, moderno y responsive.
- `js/app.js` — lee los datos desde `data/cursos.json` y renderiza todo en pantalla.
- `data/cursos.json` — los datos de prueba generados por la IA: **9 cursos, 4 categorías y 5 instructores**.

El front funciona solo con un servidor local: `python -m http.server 3000` dentro de `front/`.

### El backend que fui escribiendo (mi parte)

**Paso 1 — Entorno virtual:** creé el `venv` con `python -m venv venv` para aislar las dependencias de mi proyecto.

**Paso 2 — Paquetes instalados:** con el venv activado instalé `Django` y `django-filter` (este último es el **paquete externo** que pide la rúbrica para filtros y búsqueda):

```
asgiref==3.12.1
Django==6.1
django-filter==26.1
sqlparse==0.6.0
tzdata==2026.3
```

Las guardé en `requirements.txt`.

**Paso 3 — Proyecto y app:** tuve un problema: `django-admin` no se reconocía en Windows (faltaba el ejecutable), así que usé el comando oficial alternativo `python -m django startproject config .`. El punto (`.`) es importante porque crea el proyecto en la carpeta actual. Luego creé la app con `python manage.py startapp cursos`.

**Paso 4 — Modelos con relaciones (indicador 7):** escribí en `cursos/models.py` los tres modelos:
- `Categoria`: nombre, descripcion.
- `Instructor`: nombre, especialidad, email, anios_experiencia.
- `Curso`: titulo, slug, descripcion, nivel (con choices Básico/Intermedio/Avanzado), duracion_horas, precio, y dos **ForeignKey** hacia Categoria e Instructor (relación "muchos cursos a una categoría/instructor").

Detalle: los niveles en el modelo tienen que coincidir exactamente con el JSON (con tilde en "Básico"), sino Django rechaza el dato al cargarlo.

**Paso 5 — Registro de la app y migraciones:** al ejecutar `makemigrations` me salió `No installed app with label 'cursos'`, porque faltaba registrar la app. Agregué `'cursos'` y `'django_filters'` a `INSTALLED_APPS` en `config/settings.py` y las migraciones funcionaron:

```
Migrations for 'cursos':
  cursos\migrations\0001_initial.py
    + Create model Categoria
    + Create model Instructor
    + Create model Curso
```

Y `migrate` creó todas las tablas de la base de datos.

---

## Próximos pasos (lo que sigue)

- [ ] Crear el management command `cargar_datos` que lee `cursos.json` y puebla la base de datos.
- [ ] Ejecutarlo y verificar que los datos quedaron cargados.
- [ ] Convertir el front en templates de Django (base, listado, detalle).
- [ ] Vistas, urls y admin.
- [ ] Revisar los 12 indicadores de la rúbrica al 100%.

---

## Cómo correr el proyecto

**Front solo (sin Django):**
```
cd front
python -m http.server 3000
```
→ http://localhost:3000

**Django:**
```
venv\Scripts\Activate.ps1
python manage.py runserver
```
→ http://127.0.0.1:8000