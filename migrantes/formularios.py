from django.forms import ModelForm
from .models import migrantes
class Formulario_Migrante(ModelForm):
    class Meta:
        model = migrantes
        fields = ('nombre_completo', 'pais_origen','edad','fecha_migracion','documento')
        labels = {
            'nombre_completo':'Nombre Completo',
            'pais_origen':'Pais de Origen',
            'fecha_migracion':'Fecha de migración',
            'documento':'Documento'

        }
    # def __init__(self, *args, **kwargs):
    #     super(Formulario_Migrante,self).__init__(*args, **kwargs)
    #     self.fields['nombre_completo'] = "Select    "
    
