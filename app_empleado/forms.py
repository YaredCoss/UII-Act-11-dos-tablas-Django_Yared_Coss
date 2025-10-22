from django import forms 
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado 
        fields = ["nombre",'apellido','puesto','salario','telefono','correo','foto_empleado']