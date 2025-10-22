from django.db import models

# Create your models here.
class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    foto_empleado = models.ImageField(upload_to='img_empleado/', blank=True, null=True)
    
    def __str__(self):
        return self.nombre 
    
    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"

class Transporte(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=100)
    capacidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    horario = models.TimeField()
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name="transportes")

    def __str__(self):
        return f"{self.tipo} - {self.empleado.nombre}"