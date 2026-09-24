# PROGRESO — Directorio de Cursos (Eval 1)

> Cada vez que se complete un paso, marcarlo aquí. Última actualización: 20-09-2026

## Fase 1 — Frontend (la hace el agente)

- [x] 1.1 Crear `front/data/cursos.json` con datos de prueba generados por IA (indicador 11)
- [x] 1.2 Crear `front/css/style.css` (estilo verde esmeralda, responsive)
- [x] 1.3 Crear `front/js/app.js` (carga JSON, render, filtros, buscador)
- [x] 1.4 Crear `front/index.html` (hero + grilla + filtros por categoría + búsqueda)
- [x] 1.5 Crear `front/detalle.html` (ficha del curso + instructor + relacionados)
- [x] 1.6 Probar front standalone con `python -m http.server 3000`

## Fase 2 — Backend Django (la hace el usuario, guiado por el agente)

- [x] 2.1 Crear entorno virtual e instalar `Django` y `django-filter` (indicador 3)
- [x] 2.2 Crear proyecto Django y la app `cursos` (indicador 4 y 6)
- [x] 2.3 Escribir modelos `Categoria`, `Instructor`, `Curso` con relaciones FK (indicador 7)
- [x] 2.4 Hacer migraciones y crear la BD (indicador 6)
- [x] 2.5 Crear el management command `cargar_datos` que lee el JSON y puebla la BD (indicador 2 y 11)
- [x] 2.6 Ejecutar `cargar_datos` y verificar datos en la BD

## Fase 3 — Conexión front ↔ Django (la hace el usuario, guiado)

- [x] 3.1 Configurar `static/` para CSS y JS (indicador 8)
- [x] 3.2 Convertir los HTML en templates Django: `base.html`, `index.html`, `detalle.html`
- [x] 3.3 Crear vistas de listado con búsqueda y filtros (GET) y de detalle por slug (indicador 2 y 5)
- [x] 3.4 Crear las urls y conectarlas con `{% url %}` (indicador 5)
- [x] 3.5 Registrar los modelos en el admin (prepara eval 2)
- [x] 3.6 Probar todo con `python manage.py runserver`
- [x] 3.7 Integrar imágenes de Pixabay en tarjetas y detalle, adaptadas para móviles y PC

## Fase 4 — Verificación de la rúbrica (100%)

- [x] 4.1 Indicador 1: identificar variables y operaciones (explicación del código)
- [x] 4.2 Indicador 2: instrucciones, estructuras y operadores (vistas y comandos)
- [x] 4.3 Indicador 3: paquetes externos (`django-filter`)
- [x] 4.4 Indicador 4: aplicación Django funcional
- [x] 4.5 Indicador 5: modelo MVC aplicado (separación models/views/templates)
- [x] 4.6 Indicador 6: entorno Django configurado y documentado
- [x] 4.7 Indicador 7: Django Models con relaciones
- [x] 4.8 Indicador 8: vistas y templates integrados
- [x] 4.9 Indicador 9: tecnologías del lado del servidor
- [x] 4.10 Indicador 10: uso de IA documentado (prompts usados)
- [x] 4.11 Indicador 11: datos de prueba generados y usados con IA
- [x] 4.12 Indicador 12: protocolos, hosting y dominios explicados

## Fase 5 — Evaluación 2: Framework Back End (Persistencia, CRUD, Auth y Seguridad)

- [x] 5.1 Configuración de base de datos (`settings.py` / MySQL o SQLite avanzado) y migraciones
- [x] 5.2 Personalización profesional de Django Admin (`list_display`, `list_filter`, `search_fields`, `readonly_fields`)
- [x] 5.3 Creación de formularios con `ModelForm` (`CursoForm` con validaciones de servidor y estilos esmeralda)
- [x] 5.4 Implementación de vista y plantilla para Crear curso (**Create** vía `/cursos/nuevo/`)
- [x] 5.5 Refactorización y confirmación de vistas de Listado y Detalle (**Read**)
- [x] 5.6 Implementación de vista y plantilla para Editar curso (**Update** vía `/curso/<slug>/editar/`)
- [x] 5.7 Implementación de vista y plantilla para Eliminar curso (**Delete** vía confirmación POST en `/curso/<slug>/eliminar/`)
- [x] 5.8 Sistema de autenticación de usuarios: login, logout y redirecciones
- [x] 5.9 Protección de vistas CRUD de modificación con el decorador `@login_required`
- [x] 5.10 Blindaje de seguridad en todos los formularios con token `{% csrf_token %}` y manejo de sesiones
- [x] 5.11 Auditoría crítica y documentación de prompts de IA utilizados
- [x] 5.12 Registro continuo en `README.md` bajo la nueva sección "Unidad 2 / Evaluación 2" detallando las diferencias e innovaciones frente a la Unidad 1
- [x] 5.13 Extender Django Admin con `TabularInline` (cursos en Categoria e Instructor) y formateo de precios (Criterio 2.1.2 — Nivel 4 Destacado)
- [x] 5.14 Robustez del CRUD con `django.contrib.messages`, alertas visuales y manejo de excepciones (Criterio 2.1.3 — Nivel 4 Destacado)
- [x] 5.15 Configurar políticas avanzadas de expiración de sesión y seguridad de cookies en `settings.py` (Criterio 5 — Nivel 4 Destacado)
- [x] 5.16 Implementar manejo de colecciones en sesión HTTP (`request.session`) para cursos visitados o favoritos (Actividad Práctica Obligatoria)
- [x] 5.17 Refactorización limpia de componentes visuales (CSS de alertas desacoplado de templates HTML) y resolución de advertencias de linter en runtime

## Fase 6 — Evaluación 3: API RESTful con Django REST Framework y JWT

- [x] 6.1 Instalación de dependencias: `djangorestframework`, `djangorestframework-simplejwt` y `python-dotenv` en `venv`
- [x] 6.2 Blindaje de credenciales: creación de `.env` (ignorado en `.gitignore`) y `.env.example`
- [x] 6.3 Configuración en `settings.py`: carga de `.env`, registro de apps y configuración de `REST_FRAMEWORK` + `SIMPLE_JWT`
- [x] 6.4 Creación de serializadores explícitos (`cursos/serializers.py`) para `Categoria`, `Instructor` y `Curso` (sin `fields = '__all__'`)
- [x] 6.5 Creación de ViewSets (`cursos/api_views.py`) con `ModelViewSet`, filtros y búsqueda
- [x] 6.6 Creación de enrutador `DefaultRouter` (`cursos/api_urls.py`) y conexión en `config/urls.py` con endpoints `/api/v1/` y JWT (`/api/token/`)
- [x] 6.7 Verificación semántica de endpoints (códigos 200, 201, 204, 400, 401, 404) y suite de pruebas (`pruebas_api.http`)
- [x] 6.8 Consumo desde el frontend mediante JavaScript (`fetch()`) para desacoplamiento cliente-servidor (`templates/catalogo_api.html`)
- [x] 6.9 Documentación y preparación de defensa: `pasos_unidad_3.md` y actualización de `README.md` bajo "Unidad 3 / Evaluación 3"
- [x] 6.10 Consumo e integración de API REST externa (`mindicador.cl` para conversión monetaria en tiempo real en la ficha de detalle y endpoint proxy `/api/v1/indicadores/`)

## Prompts de IA documentados (indicador 10)

- **Prompt Unidad 1 (Datos de prueba - Indicador 11):** "Genera un JSON con 9 cursos, 5 instructores y 4 categorías para un directorio de cursos, en español, con campos id, titulo, slug, descripcion, nivel, duracion_horas, precio, categoria_id, instructor_id" → resultado en `front/data/cursos.json`.
- **Prompt Unidad 2 (Formularios y Validación en Servidor):** "Crea un ModelForm para Curso con validaciones de servidor para precio >= 0 y duración > 0, autogeneración de slug único mediante slugify y widgets con clases CSS personalizadas para formularios responsivos verde esmeralda".
- **Prompt Unidad 2 (Seguridad y Control de Acceso):** "Estructura el flujo de autenticación nativo con django.contrib.auth, implementa protección de vistas de escritura/modificación/borrado mediante decorador @login_required, formularios POST blindados con {% csrf_token %} y redirecciones seguras de sesión".
- **Prompt Unidad 3 (API RESTful y Serialización Segura):** "Genera los ModelSerializer para Categoria, Instructor y Curso con Django REST Framework, listando los campos explícitamente sin usar `fields = '__all__'`, agregando validaciones de servidor para precio y duración, y enriqueciendo el JSON con campos de lectura para nombres de categoría e instructor".
- **Prompt Unidad 3 (Seguridad Stateless con JWT):** "Configura autenticación stateless basada en JSON Web Tokens (JWT) con djangorestframework-simplejwt, protegiendo credenciales sensibles con variables de entorno python-dotenv, estableciendo permisos IsAuthenticatedOrReadOnly y configurando endpoints para obtención y refresco de tokens".
- **Auditoría Crítica Humana (Unidad 3):**
  1. *Riesgo de exposición silenciosa:* Se prohibió expresamente `fields = '__all__'` en todos los serializadores para no filtrar campos internos o sensibles.
  2. *Riesgo de alucinación de campos:* Se cotejó que cada campo en `fields` exista literalmente en `cursos/models.py`.
  3. *Seguridad de JWT:* Se verificó que ningún dato sensible (como contraseñas o hashes) viaje en el payload Base64 del JWT.
  4. *Protección de credenciales:* Se extrajo la `SECRET_KEY` de `settings.py` hacia `.env`, garantizando que quede excluida del repositorio de GitHub.

## Cómo abrir cada parte

- Front standalone: `python -m http.server 3000` dentro de `front/` → http://localhost:3000
- Django (desde fase 2): `python manage.py runserver` → http://127.0.0.1:8000

## Repositorio GitHub

- Repositorio: `https://github.com/vickotoAguilera/proyecto-django-front-mas-back.git`
- Rama principal: `main`
- **Regla de actualización:** en cada push se actualiza `README.md` (diario del estudiante en primera persona). Durante esta fase se registra bajo **"Unidad 2 / Evaluación 2"**, destacando claramente qué cosas nuevas se construyeron en comparación a la Unidad 1.
- `pasos.md` y `pasos_*.md` (guías de defensa) NO se suben: están en `.gitignore`.
- Push con token: `git remote add origin https://vickotoAguilera:<TOKEN>@github.com/vickotoAguilera/proyecto-django-front-mas-back.git` (el token vive solo en el git config local, nunca en archivos del repo).