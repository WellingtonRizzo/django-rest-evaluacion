# Generated by Django 5.0.7 on 2024-07-14 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoRestApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transformeddata',
            name='nombre_completo',
            field=models.CharField(max_length=255),
        ),
    ]
