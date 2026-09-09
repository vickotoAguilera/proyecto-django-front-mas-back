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

**Paso 6 — Comando de carga de datos desde JSON (indicador 2 y 11):** creé el management command `cursos/management/commands/cargar_datos.py` que lee el archivo `front/data/cursos.json` y puebla la base de datos usando `update_or_create`. Lo ejecuté con `python manage.py cargar_datos` y cargó exitosamente:
- 4 Categorías
- 5 Instructores
- 9 Cursos

**Paso 7 — Panel de Administración (prepara Eval 2):** registré los modelos en `cursos/admin.py` usando `@admin.register` con filtros (`list_filter`), buscadores (`search_fields`) y `prepopulated_fields` para el slug. Creé el superusuario con `python manage.py createsuperuser`.

**Paso 8 — Configuración de Static y Templates (indicador 8):** configuré `BASE_DIR / 'templates'` en `TEMPLATES['DIRS']` y `STATICFILES_DIRS` en `config/settings.py`. Copié los estilos CSS a `static/css/style.css`.

**Paso 9 — Plantillas Django (MVT, indicador 5 y 8):**
- `templates/base.html`: plantilla base con herencia (`{% block content %}`), navbar, estilos con `{% static %}` y enlaces dinámicos con `{% url %}`.
- `templates/index.html`: catálogo completo con buscador, filtros dinámicos por categoría, estadísticas y tarjetas de cursos.
- `templates/detalle.html`: ficha individual del curso con datos del instructor y cursos relacionados de la misma categoría.

**Paso 10 — Vistas y URLs (indicador 2, 5 y 8):**
- Creé las vistas en `cursos/views.py`: `index` (con búsqueda `Q`, filtros por categoría y estadísticas) y `detalle_curso` (por slug, con cursos relacionados).
- Conecté las rutas en `cursos/urls.py` e incluí la app en `config/urls.py`.
- Probé todo con `python manage.py runserver` en `http://127.0.0.1:8000/` funcionando al 100%.

**Paso 11 — Ajustes finales de código y verificación general:**
- Realicé una revisión completa de los modelos, vistas y rutas para asegurar que todo estuviera correctamente estructurado, validando consultas del ORM y preparando la arquitectura de red para la evaluación.

**Paso 12 — Integración de imágenes temáticas desde Pixabay y diseño responsivo para móviles y PC:**
- **Situación inicial:** El sitio contaba con una estructura funcional completa, pero las tarjetas estaban sin imágenes (solo texto e insignias).
- **Intervención con IA (Gemini 3.8):** Como parte del **Indicador 10** (uso de herramientas de IA como apoyo técnico), le di a **Gemini 3.8** la instrucción precisa de buscar imágenes específicas y libres de derechos en Pixabay para cada materia (Python, Django, JavaScript, UX/UI, Machine Learning, SQL, Marketing Digital, APIs REST y Frontend), adaptando el diseño para que las fotos se vean completas y uniformes tanto en computadores como en celulares.
- **Implementación técnica:**
  - Descarga y almacenamiento local en `static/img/cursos/` y `front/img/cursos/` para garantizar funcionamiento offline y standalone.
  - Carátulas con altura fija (`185px`), proporción `16 / 9`, contención estricta (`overflow: hidden`), ajuste `object-fit: cover` y badges flotantes.
  - Media queries responsivas (`@media (max-width: 560px)`) para evitar cualquier desborde en pantallas móviles.

### Evidencias del proceso (Indicadores 10 y 11)

#### 1. Estado inicial — Catálogo sin imágenes
Las tarjetas presentaban únicamente la información textual y las etiquetas de categoría y nivel:
![Catálogo inicial sin imágenes](evidencias/imagen-muestra-sin-imagenes.jpg)

#### 2. Prompt entregado a Gemini 3.8
Captura de la instrucción proporcionada a la IA para buscar imágenes en Pixabay según el contenido de cada curso y adaptarlas a PC y celulares:
![Prompt proporcionado a Gemini 3.8](evidencias/imagen-prompt-gemini-3-8.jpg)

#### 3. Resultado final — Tarjetas con fotos temáticas adaptadas a PC y móviles
Así quedó el catálogo con las imágenes temáticas integradas, diseño responsivo y efectos visuales modernos:
![Catálogo con fotos desde Pixabay](evidencias/cards-con-fotos-desde-pixabay.jpg)

---

## Arquitectura, Protocolos y Despliegue (Indicador 12)

- **Protocolo de comunicación:** en desarrollo la aplicación corre sobre **HTTP** estándar. El cliente (navegador) solicita recursos al servidor local de Django (`127.0.0.1` o `localhost`) en el puerto `8000` mediante peticiones GET.
- **Servicio de Hosting recomendado:** para pasar a producción se propone el despliegue en un PaaS como **Render** o **PythonAnywhere**, ejecutando la aplicación con un servidor WSGI de producción como **Gunicorn** y una base de datos PostgreSQL gestionada.
- **Dominio y Seguridad:** se conectaría un dominio personalizado (ej. `midirectorio.cl`) configurando registros DNS de tipo A y CNAME hacia el hosting, implementando **HTTPS** mediante certificados SSL/TLS automáticos (Let's Encrypt) para garantizar el cifrado de datos.

---

## Estado del Proyecto

- [x] Crear datos de prueba en JSON con IA (indicador 11).
- [x] Crear el frontend standalone (`front/`).
- [x] Crear entorno virtual e instalar Django y django-filter (indicador 3 y 6).
- [x] Modelos Django con relaciones ForeignKey (indicador 7).
- [x] Migraciones y creación de la BD SQLite (indicador 6).
- [x] Management command `cargar_datos` (indicador 2 y 11).
- [x] Registro en Django Admin con superusuario.
- [x] Configuración de templates y archivos estáticos (indicador 8).
- [x] Vistas y URLs de catálogo y detalle (indicador 2, 5 y 8).
- [x] Pruebas en servidor local `runserver` (indicador 4 y 9).
- [x] Últimos ajustes y verificación general en el código del backend.
- [x] Integración de imágenes temáticas desde Pixabay y diseño responsivo (PC y móviles).
- [x] Documentación de protocolos, hosting y despliegue (indicador 12).

---

## Cómo correr el proyecto

### Servidor Django (Backend + Frontend integrado)

**Opción 1 — Directa con el entorno virtual (Recomendada en Windows):**
Garantiza usar el Python y las librerías del `venv` (`django-filter`), evitando conflictos si PowerShell llama al Python global del sistema:
```powershell
.\venv\Scripts\python.exe manage.py runserver
```

**Opción 2 — Activando el entorno virtual previamente:**
```powershell
.\venv\Scripts\Activate.ps1
python manage.py runserver
```

- **Web principal:** http://127.0.0.1:8000/
- **Panel de administración:** http://127.0.0.1:8000/admin/

---

### (Opcional) Frontend Standalone (Sin Django)
Para visualizar el frontend estático leyendo de forma independiente desde `front/data/cursos.json`:
```powershell
cd front
python -m http.server 3000
```
- **Web:** http://localhost:3000

---

# Unidad 2 / Evaluación 2 — Framework Back End (Diario de trabajo)

> Aquí registro la evolución de mi proyecto durante la **Unidad 2**, transformando el sitio web inicial de la Unidad 1 en una aplicación completa con persistencia relacional activa, operaciones CRUD interactivas, formularios de servidor, Django Admin profesional, autenticación de usuarios y blindaje de seguridad web.

### Comparativa: ¿Qué teníamos en la Unidad 1 vs qué incorporamos en la Unidad 2?

| Área / Característica | Unidad 1 (Evaluación 1) | Unidad 2 (Evaluación 2) |
| :--- | :--- | :--- |
| **Gestión de datos** | Datos iniciales leídos desde un JSON fijo y cargados con un comando a SQLite | Persistencia activa en base de datos con manipulación directa mediante el ORM de Django |
| **Operaciones con datos** | Exclusivamente lectura (`Read`): listado y ficha de detalle | Operaciones **CRUD completas** desde la web: Crear, Leer, Actualizar y Eliminar |
| **Formularios web** | Inexistentes en la interfaz pública | Formularios automáticos vinculados al modelo con validación en servidor (`ModelForm`) |
| **Panel de Administración** | Registro básico de modelos | `ModelAdmin` profesional con columnas personalizadas (`list_display`), filtros (`list_filter`) y búsquedas (`search_fields`) |
| **Autenticación de usuarios** | Solo superusuario para ingresar a `/admin/` | Sistema de autenticación de usuarios (login, logout, control de acceso con `@login_required`) |
| **Seguridad web** | Navegación básica sin estado | Blindaje estricto contra ataques CSRF (`{% csrf_token %}` en formularios POST) y manejo de sesiones en servidor |

---

### Para recordar: Si en algún momento necesito migrar los datos a MySQL tengo que hacer esto

Si en la evaluación o en clase el profesor solicita conectar la aplicación directamente a **MySQL** (por ejemplo mediante WAMP, XAMPP o Laragon), estos son los pasos exactos que debemos ejecutar en ese instante:

#### 1. Iniciar el servidor MySQL
- Abrir WAMP o XAMPP y presionar **Start** en el servicio **MySQL** para que quede activo y escuchando en el puerto local estándar `3306`.

#### 2. Crear la base de datos en MySQL
- Ingresar a phpMyAdmin (`http://localhost/phpmyadmin`) o abrir la consola de MySQL y ejecutar la sentencia SQL:
  ```sql
  CREATE DATABASE cursos_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
  ```

#### 3. Instalar el conector en el entorno virtual
- Con el terminal posicionado en la carpeta del proyecto, instalar el driver de conexión:
  ```powershell
  .\venv\Scripts\pip install mysqlclient
  ```
  *(Nota técnica: Si en Windows `mysqlclient` diera error de compilación C++, la alternativa directa y 100% pura de Python es instalar `PyMySQL` ejecutando `.\venv\Scripts\pip install pymysql` y agregando dos líneas al inicio de `config/__init__.py`: `import pymysql; pymysql.install_as_MySQLdb()`).*

#### 4. Cambiar el bloque `DATABASES` en `config/settings.py`
- En el archivo `config/settings.py`, comentar el bloque de SQLite y descomentar/activar el bloque de MySQL con sus 6 parámetros:
  ```python
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'cursos_db',
          'USER': 'root',        # Usuario predeterminado en WAMP/XAMPP
          'PASSWORD': '',            # Contraseña (vacía por defecto en WAMP/XAMPP)
          'HOST': '127.0.0.1',       # Loopback / Localhost
          'PORT': '3306',            # Puerto de red estándar de MySQL
      }
  }
  ```

#### 5. Ejecutar las migraciones en MySQL
- Para que Django cree todas las tablas automáticamente en la base de datos MySQL:
  ```powershell
  .\venv\Scripts\python.exe manage.py migrate
  ```

#### 6. Cargar los datos iniciales y crear el administrador
- Poblar la base de datos desde nuestro archivo JSON con el comando que construimos:
  ```powershell
  .\venv\Scripts\python.exe manage.py cargar_datos
  ```
- Crear el superusuario para ingresar a `/admin/`:
  ```powershell
  .\venv\Scripts\python.exe manage.py createsuperuser
  ```
- Iniciar el servidor:
  ```powershell
  .\venv\Scripts\python.exe manage.py runserver
  ```
- ¡Listo! Todo queda funcionando sobre MySQL sin haber tocado ni una sola línea de los modelos ni de las vistas.

---

### Registro de avances — Unidad 2 (Mi diario de desarrollo)

#### Paso 1 — Persistencia en base de datos e internacionalización (`config/settings.py`):
- Analicé los dos motores de base de datos disponibles para el proyecto: **SQLite** (ligero, embebido y portable para desarrollo) y **MySQL** (servidor cliente-servidor para producción).
- Configuré el diccionario `DATABASES` en `settings.py` dejando activo SQLite y documenté el bloque de conexión a MySQL con sus 6 parámetros obligatorios (`ENGINE`, `NAME`, `USER`, `PASSWORD`, `HOST`, `PORT`).
- Cambié la configuración de internacionalización a `LANGUAGE_CODE = 'es'` y `TIME_ZONE = 'America/Santiago'` para que el sitio, los mensajes de validación y el panel de administración hablen en español nativo con la zona horaria chilena.

#### Paso 2 — Django Admin Profesional (`cursos/admin.py`):
- Siguiendo los contenidos de la unidad, profesionalicé la administración de los modelos con la clase `ModelAdmin` y el decorador `@admin.register`.
- En `CursoAdmin` configuré `list_display` con los campos clave, `list_filter` para filtros laterales rápidos (por categoría, nivel e instructor), `search_fields` para búsqueda predictiva por texto, `prepopulated_fields` para rellenar el slug automáticamente y `list_per_page = 10` para paginación limpia.
- Personalicé los títulos corporativos del panel con `admin.site.site_header`, `admin.site.site_title` e `admin.site.index_title`.

#### Paso 3 — Creación de Formularios con `ModelForm` (`cursos/forms.py`):
- Implementé la clase `CursoForm` heredando de `forms.ModelForm`.
- Configuré en la clase interna `Meta` los campos permitidos y definí `widgets` inyectando clases CSS (`form-input`, `form-select`, `form-textarea`) para mantener la estética verde esmeralda y moderna del frontend.
- **Validaciones en el servidor:** Programé los métodos `clean_precio` (asegurando que el precio no sea negativo) y `clean_duracion_horas` (asegurando que la duración sea mayor a cero).
- **Automatización de URLs amigables:** Sobrescribí el método `save()` para que al crear un nuevo curso, el `slug` se genere automáticamente a partir del título usando la función `slugify()`, evitando colisiones con slugs duplicados.

#### Paso 4 — Solución de Favicon y recursos estáticos:
- Generé el icono esmeralda de la plataforma `favicon.ico` para la pestaña del navegador y lo vinculé en `templates/base.html`, solucionando el error `404 Not Found: /favicon.ico` en la consola de Django.

#### Paso 5 — Implementación completa del ciclo CRUD en el navegador (Create, Read, Update, Delete):
- **Create (`/curso/nuevo/`):** Programé la vista `curso_crear` que gestiona peticiones GET (entregando el formulario vacío) y peticiones POST (procesando los datos con `CursoForm`, validando en servidor y persistiendo en la base de datos con `form.save()`). Al completarse, redirige limpiamente a la ficha del curso recién creado.
- **Read (`/` y `/curso/<slug>/`):** Las vistas `index` (listado con búsqueda y filtros optimizado con `select_related`) y `detalle_curso` (ficha de detalle con `get_object_or_404`) garantizan la lectura íntegra de registros.
- **Update (`/curso/<slug>/editar/`):** Implementé la vista `curso_editar` recuperando la instancia existente con `get_object_or_404` y vinculándola al formulario mediante `form = CursoForm(..., instance=curso)`, permitiendo modificar cualquier campo y guardar los cambios con `form.save()`.
- **Delete (`/curso/<slug>/eliminar/`):** Apliqué una política de seguridad estricta para el borrado: la ruta GET presenta una pantalla de confirmación visual (`curso_confirm_delete.html`) con resumen del curso, y únicamente ante una petición POST con token de seguridad `{% csrf_token %}` ejecuta la eliminación irreversible mediante el método del ORM `curso.delete()`, redirigiendo al catálogo principal.
- **Conexión en el frontend:** Diseñé las plantillas `curso_form.html` y `curso_confirm_delete.html`, agregué el botón de acción rápida `+ Nuevo Curso` en la barra de navegación y los botones de `Editar curso` y `Eliminar` en la ficha de detalle.

#### Paso 6 — Autenticación, Control de Acceso y Blindaje de Seguridad Web:
- **Rutas y redirecciones de autenticación:** Conecté el módulo nativo `django.contrib.auth.urls` en `config/urls.py` para habilitar las vistas seguras de login y logout. Configuré en `settings.py` las directivas `LOGIN_URL = 'login'`, `LOGIN_REDIRECT_URL = 'inicio'` y `LOGOUT_REDIRECT_URL = 'inicio'`.
- **Plantilla de Login (`templates/registration/login.html`):** Diseñé la pantalla de inicio de sesión con estética verde esmeralda, soporte para el parámetro `next` (preservando la URL original solicitada para redirigir tras autenticarse), mensajes de credenciales incorrectas en español y protección mediante token CSRF.
- **Protección de vistas con `@login_required`:** Blindé las tres vistas de modificación (`curso_crear`, `curso_editar`, `curso_eliminar`) con el decorador `@login_required`. Si un usuario anónimo intenta acceder directamente escribiendo la URL en el navegador, Django lo intercepta en el servidor y lo redirige automáticamente al login.
- **Interfaz dinámica según estado de sesión:** Actualicé la barra de navegación y la ficha de detalle con condicionales `{% if user.is_authenticated %}`. Los visitantes no autenticados solo tienen permisos de lectura (`Read`) y ven el botón `Iniciar sesión`; mientras que los usuarios autenticados visualizan su insignia de usuario (`👤 admin`), el botón de cierre de sesión seguro mediante formulario POST, y las opciones operativas para crear, editar y eliminar cursos.
- **Protección contra ataques CSRF y gestión de sesiones:** Todos los formularios POST de la aplicación implementan estrictamente la etiqueta `{% csrf_token %}`, garantizando que cualquier petición maliciosa externa sea rechazada con error 403 Forbidden. El estado de autenticación se gestiona en cookies firmadas y sesiones persistidas en la base de datos.

#### Paso 7 — Uso de IA como Copiloto y Auditoría Crítica Humana (Indicadores 10 y 11):
- **Prompts técnicos formulados:**
  - *Generación de formularios y validaciones:* "Crea un ModelForm para Curso con validaciones de servidor para precio >= 0 y duración > 0, autogeneración de slug único mediante slugify y widgets con clases CSS personalizadas para formularios responsivos verde esmeralda".
  - *Blindaje de autenticación y seguridad:* "Estructura el flujo de autenticación nativo con django.contrib.auth, implementa protección de vistas de mutación mediante el decorador @login_required, formularios blindados con {% csrf_token %} y redirecciones seguras de sesión".
- **Auditoría crítica y decisiones de arquitectura tomadas por el estudiante:**
  1. *Decisión de persistencia:* Se mantuvo SQLite como base de datos activa para desarrollo rápido y portable, dejando documentada y parametrizada la configuración de MySQL en `settings.py` con sus 6 parámetros obligatorios para cuando se requiera migrar.
  2. *Auditoría de seguridad y control de acceso:* Se verificó que ninguna vista de modificación quedara accesible a usuarios anónimos y que la interfaz oculte los botones administrativos a visitantes públicos.
  3. *Auditoría de integridad relacional:* Se estableció que las eliminaciones requieran confirmación explícita mediante método POST con token CSRF, impidiendo eliminaciones accidentales o maliciosas por enlaces GET.