from django.db import models

class RawData(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.DateField()

    class Meta:
        db_table = 'raw_data'  # Asegúrate de que el nombre de la tabla coincide con el nombre en la base de datos

class NewData(models.Model):
    nombre_completo = models.CharField(max_length=100)
    edad_nominal = models.IntegerField()

    class Meta:
        db_table = 'djangoRestApp_newdata'  # Asegúrate de que el nombre de la tabla coincide con el nombre en la base de datos
