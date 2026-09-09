# AGENTS.md — Reglas del proyecto

> Lee este archivo SIEMPRE al iniciar una conversación nueva. También lee PROGRESO.md para saber qué pasos están completados.

## Contexto del proyecto

- Proyecto académico: **Directorio de Cursos** (idea 4 elegida por el usuario).
- Marco: módulo "Desarrollo de aplicaciones del lado del servidor".
- Instrumento de evaluación: `Escala_de_Apreciacion_Django_eva1.pdf` (12 indicadores, niveles 1-4).
- Hay **3 evaluaciones encadenadas**:
  1. **Eval 1 / Unidad 1 (completada):** sitio web básico que usa datos desde JSON.
  2. **Eval 2 / Unidad 2 (actual):** convertir en una app completa (CRUD, ModelForms, Admin pro, MySQL/persistencia, autenticación y CSRF).
  3. **Eval 3 / Unidad 3:** convertir en una API (Django REST Framework).
- Por eso TODO lo que se construya debe ser **escalable**: mismos modelos, misma BD, estructura limpia.

## División de roles (orden del profesor)

- **El AGENTE (yo, opencode):**
  - Hago TODO el frontend: HTML, CSS, JavaScript (carpeta `front/`).
  - Guío paso a paso al usuario en el backend de Django: explico, muestro ejemplos, reviso el código.
  - **NO escribo el código del backend por el usuario** (models, views, urls, admin, settings). El usuario debe escribirlo para poder defenderlo en la evaluación. Solo explico y corrijo.
  - Genero los datos de prueba con IA (indicador 11 de la rúbrica).
- **El USUARIO (estudiante):**
  - Escribe el backend de Django con mi guía: proyecto, app, modelos, comando de carga, vistas, urls, admin.

## Reglas fijas

1. Idioma de trabajo y del sitio: **español**.
2. Estilo visual: **verde esmeralda**, moderno, responsive, tarjetas con sombra suave.
3. El frontend (`front/`) debe funcionar **standalone**: abrirse con un servidor local (`python -m http.server 3000`) y leer sus propios datos desde `front/data/cursos.json`.
4. Los datos viven en JSON (eval 1). Luego se cargan a los modelos de Django con un management command (`cargar_datos`). Nada de escribir datos a mano en la BD.
5. Los 12 indicadores de la rúbrica deben quedar cubiertos al 100%.
6. Al terminar cada paso, actualizar `PROGRESO.md` marcando las casillas.
7. No crear archivos fuera de la estructura definida en PLAN.md sin avisar antes.
8. En cada conversación nueva: leer `AGENTS.md`, `PROGRESO.md` y, si es necesario, `PLAN.md`.
9. El proyecto se sube a GitHub en cada hito: `https://github.com/vickotoAguilera/proyecto-django-front-mas-back.git` (rama `main`, push con token en la URL del remote).
10. **Cada push actualiza `README.md`** (diario en primera persona): a partir de ahora se redacta bajo la sección **"Unidad 2 / Evaluación 2"**, detallando qué cosas nuevas se implementaron desde la Unidad 1 para evidenciar claramente la evolución del proyecto.
11. `pasos.md` y `pasos_*.md` son las guías de defensa (qué hace cada archivo y concepto) y **van en `.gitignore`**: nunca se suben.
12. Nunca escribir el token en ningún archivo del repo (solo en el git config local).

## Modelos planificados (eval 1, escalables)

- `Categoria`: nombre, descripcion.
- `Instructor`: nombre, especialidad, email, anios_experiencia.
- `Curso`: titulo, slug, descripcion, nivel, duracion_horas, precio, categoria (FK), instructor (FK).

## Paquete externo (indicador 3)

- `django-filter` para filtros y búsqueda en Django (además de Django mismo).

## Rúbrica resumida (indicadores clave)

1. Identifica variables y operaciones del lenguaje.
2. Codifica instrucciones, estructuras y operadores.
3. Codifica usando paquetes externos.
4. Implementa app sencilla en Django.
5. Aplica modelo MVC.
6. Configura entorno Django correctamente.
7. Implementa Django Models (con relaciones).
8. Implementa vistas y templates.
9. Usa tecnologías del lado del servidor.
10. Usa herramientas de IA como apoyo (el agente lo es; documentar prompts).
11. Genera y usa datos de prueba mediante IA (el JSON).
12. Relaciona la solución con protocolos, hosting y dominios.

## Cómo se sirve cada parte

- Front standalone: `python -m http.server 3000` dentro de `front/` → http://localhost:3000
- Django (fase 2 en adelante): `python manage.py runserver` → http://127.0.0.1:8000