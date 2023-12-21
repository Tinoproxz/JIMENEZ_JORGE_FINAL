from django import forms

from .models import Inscritos, Instituciones

class InscritosForm(forms.ModelForm):
    class Meta:
        model = Inscritos
        fields = ['id','nombre','telefono','id_institucion','estado','observacion']
        widgets ={
            'id': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'id_institucion': forms.Select(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'observacion':forms.Textarea(attrs={'class': 'form-control'})
        }

class InstitucionesForm(forms.ModelForm):
    class Meta:
        model = Instituciones
        fields = ['id_insti','nombre','direccion']
        widgets ={
            'id_insti': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
        }
