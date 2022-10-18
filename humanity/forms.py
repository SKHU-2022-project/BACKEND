from django import forms
from .models import ITBoard

class BoardForm(forms.ModelForm):
    class Meta:
        model = ITBoard
        fields = ['writer', 'body']