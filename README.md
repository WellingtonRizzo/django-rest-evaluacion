# Django REST y psotman Evaluación3 y4 

Este proyecto es una API RESTful creada con Django REST Framework para transformar y manejar datos de usuarios.

## Función:

- Transformación de datos: Convierte la edad de fecha a edad nominal y nombre y apellido en un solo campo.
- Obtener datos transformados: Recupera todos los datos transformados .

## Cómo usar

### Endpoints para usar en postman:

- POST /api/transform/: Transforma los datos de una tabla hacia la otra.
- GET /api/newdata/: Obtiene los datos transformados.

## Configuración

- las variables de entorno estan por separado para mayor proteccion .env.

## Requisitos

- Python 
- Django
- Django REST Framework
