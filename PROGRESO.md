# PROGRESO — Directorio de Cursos (Eval 1)

> Cada vez que se complete un paso, marcarlo aquí. Última actualización: 24-08-2026

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
- [ ] 2.5 Crear el management command `cargar_datos` que lee el JSON y puebla la BD (indicador 2 y 11)
- [ ] 2.6 Ejecutar `cargar_datos` y verificar datos en la BD

## Fase 3 — Conexión front ↔ Django (la hace el usuario, guiado)

- [ ] 3.1 Configurar `static/` para CSS y JS (indicador 8)
- [ ] 3.2 Convertir los HTML en templates Django: `base.html`, `index.html`, `detalle.html`
- [ ] 3.3 Crear vistas de listado con búsqueda y filtros (GET) y de detalle por slug (indicador 2 y 5)
- [ ] 3.4 Crear las urls y conectarlas con `{% url %}` (indicador 5)
- [ ] 3.5 Registrar los modelos en el admin (prepara eval 2)
- [ ] 3.6 Probar todo con `python manage.py runserver`

## Fase 4 — Verificación de la rúbrica (100%)

- [ ] 4.1 Indicador 1: identificar variables y operaciones (explicación del código)
- [ ] 4.2 Indicador 2: instrucciones, estructuras y operadores (vistas y comandos)
- [ ] 4.3 Indicador 3: paquetes externos (`django-filter`)
- [ ] 4.4 Indicador 4: aplicación Django funcional
- [ ] 4.5 Indicador 5: modelo MVC aplicado (separación models/views/templates)
- [ ] 4.6 Indicador 6: entorno Django configurado y documentado
- [ ] 4.7 Indicador 7: Django Models con relaciones
- [ ] 4.8 Indicador 8: vistas y templates integrados
- [ ] 4.9 Indicador 9: tecnologías del lado del servidor
- [ ] 4.10 Indicador 10: uso de IA documentado (prompts usados)
- [ ] 4.11 Indicador 11: datos de prueba generados y usados con IA
- [ ] 4.12 Indicador 12: protocolos, hosting y dominios explicados

## Prompts de IA documentados (indicador 10)

- Prompt para generar los datos de prueba del JSON (indicador 11): "Genera un JSON con 9 cursos, 5 instructores y 4 categorías para un directorio de cursos, en español, con campos id, titulo, slug, descripcion, nivel, duracion_horas, precio, categoria_id, instructor_id" → resultado en `front/data/cursos.json`.

## Cómo abrir cada parte

- Front standalone: `python -m http.server 3000` dentro de `front/` → http://localhost:3000
- Django (desde fase 2): `python manage.py runserver` → http://127.0.0.1:8000

## Repositorio GitHub

- Repositorio: `https://github.com/vickotoAguilera/proyecto-django-front-mas-back.git`
- Rama principal: `main`
- **Regla:** en cada push se actualiza `README.md` con los pasos nuevos completados (en primera persona, como diario del estudiante).
- `pasos.md` (guía de defensa) NO se sube: está en `.gitignore`.
- Push con token: `git remote add origin https://vickotoAguilera:<TOKEN>@github.com/vickotoAguilera/proyecto-django-front-mas-back.git` (el token vive solo en el git config local, nunca en archivos del repo).