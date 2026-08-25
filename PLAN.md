# PLAN — Directorio de Cursos (Evaluación 1)

> Proyecto académico: módulo "Desarrollo de aplicaciones del lado del servidor".
> Instrumento: `Escala_de_Apreciacion_Django_eva1.pdf` (12 indicadores).

## Objetivo

Construir un **sitio web básico en Django que usa datos desde JSON**, escalable a las siguientes evaluaciones:

- **Eval 1 (esta):** sitio básico con datos en JSON.
- **Eval 2:** convertir en una app con funcionalidades completas.
- **Eval 3:** convertir en una API con Django REST Framework.

Para eso: mismos modelos, misma base de datos, estructura limpia.

## División de roles (orden del profesor)

| Quién | Qué hace |
|-------|----------|
| **Agente (opencode)** | TODO el frontend: HTML, CSS, JS en `front/`. Guía al usuario en el backend. Genera datos de prueba con IA. |
| **Usuario (estudiante)** | Escribe el backend de Django: proyecto, app, modelos, comando de carga, vistas, urls, admin. |

## Estructura de archivos

```
pagina por django/
├── AGENTS.md                  # Reglas del proyecto (leer siempre)
├── PROGRESO.md                # Checklist de avance
├── PLAN.md                    # Este plan
├── README.md                  # Diario del proyecto en primera persona (se actualiza en cada push)
├── pasos.md                   # Guía de defensa (EN .gitignore, nunca se sube)
├── .gitignore                 # Excluye venv, BD, pasos.md, etc.
├── requirements.txt           # Dependencias del proyecto
├── Escala_de_Apreciacion_Django_eva1.pdf
├── front/                     # Frontend standalone (lo hace el agente)
│   ├── index.html             # Listado de cursos con filtros y buscador
│   ├── detalle.html           # Ficha completa del curso
│   ├── css/style.css          # Estilo verde esmeralda
│   ├── js/app.js              # Render, filtros, buscador
│   └── data/cursos.json       # Datos de prueba generados con IA
├── config/                    # Proyecto Django (lo hace el usuario)
│   └── settings.py, urls.py, wsgi.py, asgi.py
├── cursos/                    # App Django (lo hace el usuario)
│   ├── models.py              # Categoria, Instructor, Curso
│   ├── migrations/            # Historial de la BD
│   └── data/cursos.json       # Copia del JSON para cargar datos
├── manage.py
└── venv/                      # Entorno virtual (en .gitignore)
```

Luego, cuando el usuario cree el backend Django (fuera de `front/`), el front se convierte en templates.

## Fase 1 — Frontend (LA HACE EL AGENTE)

- `front/index.html`: hero, buscador, filtros por categoría, grilla de tarjetas.
- `front/detalle.html`: ficha del curso + tarjeta del instructor + cursos relacionados.
- `front/css/style.css`: verde esmeralda, moderno, responsive.
- `front/js/app.js`: lee `data/cursos.json`, renderiza y filtra.
- `front/data/cursos.json`: datos de prueba (categorías, instructores, cursos) generados con IA.

El front debe verse **solo**: `python -m http.server 3000` dentro de `front/` → http://localhost:3000

## Fase 2 — Backend en Django (LA HACE EL USUARIO, guiado)

1. Crear entorno virtual e instalar `Django` y `django-filter` (indicador 3: paquete externo).
2. `django-admin startproject` + `startapp cursos`.
3. Crear modelos con **relaciones** (indicador 7):
   - `Categoria`: nombre, descripcion.
   - `Instructor`: nombre, especialidad, email, anios_experiencia.
   - `Curso`: titulo, slug, descripcion, nivel, duracion_horas, precio, categoria (FK), instructor (FK).
4. Copiar/adaptar los datos a un JSON accesible por Django (indicador 11: datos generados con IA).
5. Management command `cargar_datos` que lee el JSON y puebla la BD (nada de datos a mano).

## Fase 3 — Conexión front ↔ Django (LA HACE EL USUARIO, guiado)

6. Convertir los HTML de `front/` en templates Django (`base.html`, `index.html`, `detalle.html`).
7. Configurar `static/` para CSS y JS.
8. Vistas: listado con búsqueda y filtros (GET), detalle por slug.
9. URLs conectadas con `{% url %}` en las plantillas.
10. Registrar modelos en el admin (prepara la eval 2).

## Fase 4 — Verificación de la rúbrica (100%)

Repasar los 12 indicadores con el usuario y marcar evidencias en `PROGRESO.md`.

## Rúbrica → evidencia esperada

| # | Indicador | Dónde se evidencia |
|---|-----------|--------------------|
| 1 | Identifica variables y operaciones | Explicación del código con el usuario |
| 2 | Codifica instrucciones, estructuras y operadores | Vistas, comandos, templates |
| 3 | Usa paquetes externos | `django-filter`, `Django` (pip install) |
| 4 | Implementa app sencilla en Django | Proyecto completo funcional |
| 5 | Aplica modelo MVC | Separación models / views / templates |
| 6 | Configura entorno Django | venv, settings, runserver documentado |
| 7 | Django Models con relaciones | Categoria, Instructor, Curso con FK |
| 8 | Vistas y templates | Listado + detalle renderizados por Django |
| 9 | Tecnologías del lado del servidor | Python, Django, manejo de peticiones HTTP |
| 10 | Usa IA como apoyo | Este agente; prompts documentados en PROGRESO.md |
| 11 | Genera y usa datos de prueba con IA | `cursos.json` + comando `cargar_datos` |
| 12 | Protocolos, hosting y dominios | HTTP/localhost explicados; alternativas de despliegue |