from django import forms
from django.db.models import fields

from .models import *

class RespuestaBlogForm(forms.ModelForm):
    """Form definition for Detalle."""

    class Meta:
        """Meta definition for Detalleform."""

        model = RespuestaBlog
        fields = '__all__'
        exclude = [
            'blog'
        ]
        widgets = {
            'comentario': forms.Textarea(attrs={'rows': '3'}),
        }
