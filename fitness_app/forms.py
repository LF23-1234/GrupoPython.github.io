from django import forms
from .models import Habito

class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Tu nombre'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Tu email'
    }))
    mensaje = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Tu mensaje',
        'rows': 5
    }))

class HabitoForm(forms.ModelForm):
    class Meta:
        model = Habito
        fields = ['ejercicio_realizado', 'duracion_minutos', 'calorias_quemadas', 'notas']
        widgets = {
            'ejercicio_realizado': forms.TextInput(attrs={'class': 'form-control'}),
            'duracion_minutos': forms.NumberInput(attrs={'class': 'form-control'}),
            'calorias_quemadas': forms.NumberInput(attrs={'class': 'form-control'}),
            'notas': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }