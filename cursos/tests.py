from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Categoria, Instructor, Curso

# suite de pruebas automatizadas para la API RESTful de la Unidad 3
# cubre los criterios de evaluacion: autenticacion JWT, codigos HTTP semanticos, serializacion JSON y validaciones
class DirectorioCursosAPITests(APITestCase):

    def setUp(self):
        # aca creo el usuario de prueba para autenticacion JWT
        self.user = User.objects.create_user(
            username='estudiante_test',
            password='PasswordSeguro123!'
        )

        # aca creo la categoria y el instructor iniciales para asociar al curso
        self.categoria = Categoria.objects.create(
            nombre='Programación Back End',
            descripcion='Cursos de desarrollo de servidores y APIs'
        )

        self.instructor = Instructor.objects.create(
            nombre='Ada Lovelace',
            especialidad='Arquitectura de Software',
            email='ada@example.com',
            anios_experiencia=10
        )

        # aca creo un curso inicial en base de datos
        self.curso = Curso.objects.create(
            titulo='Curso de Prueba Django REST',
            slug='curso-de-prueba-django-rest',
            descripcion='Aprende a construir APIs RESTful profesionales con DRF.',
            nivel='Básico',
            duracion_horas=24,
            precio=29990,
            categoria=self.categoria,
            instructor=self.instructor
        )

    # 1. verifica consulta publica del catalogo (GET 200 OK con JSON paginado)
    def test_listado_cursos_publico(self):
        response = self.client.get('/api/v1/cursos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # verifica que la respuesta incluya paginacion y resultados
        self.assertIn('results', response.data)
        self.assertGreaterEqual(len(response.data['results']), 1)

    # 2. verifica consulta de detalle de curso y campos calculados de lectura (GET 200 OK)
    def test_detalle_curso_y_campos_calculados(self):
        response = self.client.get(f'/api/v1/cursos/{self.curso.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['titulo'], 'Curso de Prueba Django REST')
        # verifica los campos ReadOnlyField que enriquecen el JSON sin queries extras
        self.assertEqual(response.data['categoria_nombre'], self.categoria.nombre)
        self.assertEqual(response.data['instructor_nombre'], self.instructor.nombre)

    # 3. verifica blindaje de seguridad: rechazo de creacion sin credenciales (POST 401 Unauthorized)
    def test_creacion_sin_token_rechazada(self):
        payload = {
            'titulo': 'Curso no autorizado',
            'descripcion': 'Intento sin credenciales',
            'nivel': 'Básico',
            'duracion_horas': 10,
            'precio': 15000,
            'categoria': self.categoria.id,
            'instructor': self.instructor.id
        }
        response = self.client.post('/api/v1/cursos/', payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # 4. verifica obtencion de JWT y creacion exitosa de curso (POST 201 Created)
    def test_creacion_con_token_jwt(self):
        # paso 1: obtener el token JWT
        login_res = self.client.post('/api/token/', {
            'username': 'estudiante_test',
            'password': 'PasswordSeguro123!'
        }, format='json')
        self.assertEqual(login_res.status_code, status.HTTP_200_OK)
        self.assertIn('access', login_res.data)
        self.assertIn('refresh', login_res.data)
        access_token = login_res.data['access']

        # paso 2: consumir el endpoint protegido adjuntando la cabecera Authorization: Bearer <Token>
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        nuevo_curso_payload = {
            'titulo': 'Microservicios y Docker en Python',
            'descripcion': 'Diseño y despliegue de contenedores y servicios web.',
            'nivel': 'Avanzado',
            'duracion_horas': 40,
            'precio': 45000,
            'categoria': self.categoria.id,
            'instructor': self.instructor.id
        }
        response = self.client.post('/api/v1/cursos/', nuevo_curso_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['titulo'], 'Microservicios y Docker en Python')
        # verifica que el servidor autogenero el slug
        self.assertTrue(response.data['slug'].startswith('microservicios-y-docker-en-python'))

    # 5. verifica validacion de negocio en el Serializer (precio negativo -> 400 Bad Request)
    def test_validacion_precio_negativo(self):
        login_res = self.client.post('/api/token/', {
            'username': 'estudiante_test',
            'password': 'PasswordSeguro123!'
        }, format='json')
        access_token = login_res.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

        payload_invalido = {
            'titulo': 'Curso con Precio Erróneo',
            'descripcion': 'El precio no puede ser negativo',
            'nivel': 'Intermedio',
            'duracion_horas': 15,
            'precio': -5000,  # valor prohibido por la regla de validacion
            'categoria': self.categoria.id,
            'instructor': self.instructor.id
        }
        response = self.client.post('/api/v1/cursos/', payload_invalido, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('precio', response.data)

    # 6. verifica respuesta consistente en JSON ante recurso inexistente (GET 404 Not Found)
    def test_recurso_inexistente_retorna_404_json(self):
        response = self.client.get('/api/v1/cursos/999999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn('detail', response.data)

    # 7. verifica endpoint de integracion externa de indicadores economicos (GET 200 OK)
    from unittest.mock import patch

    @patch('cursos.api_views.obtener_conversion_monedas')
    def test_endpoint_indicadores_economicos(self, mock_obtener_conversion):
        # mockeamos la respuesta del servicio externo para no depender de la latencia de internet durante los tests
        mock_obtener_conversion.return_value = {
            'disponible': True,
            'dolar': '950.50',
            'uf': '37.850.20',
            'precio_usd': '31.55',
            'precio_uf': '0.79',
            'fecha': '2026-10-01',
            'fuente': 'mindicador.cl',
        }
        response = self.client.get('/api/v1/indicadores/?precio=29990')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['disponible'])
        self.assertIn('dolar', response.data)
        self.assertIn('uf', response.data)
        self.assertEqual(response.data['fuente'], 'mindicador.cl')
