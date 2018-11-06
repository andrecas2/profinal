from django import forms

from .models import Comic

class ComicsForm(forms.ModelForm):

    class Meta:
        model = Comic
        fields = [
            'nombre',
            'fecha_publicacion',
            'editorial',
            'autor',

        ]
        labels = {
            'nombre': 'Nombre',
            'fecha_publicacion' : 'Fecha_publicacion',
            'editorial': 'Editorial',
            'autor': 'Autor',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_publicacion': forms.TextInput(attrs={'class': 'form-control'}),
            'editorial': forms.Select(attrs={'class': 'form-control'}),
            'autor': forms.CheckboxSelectMultiple(),
        }
