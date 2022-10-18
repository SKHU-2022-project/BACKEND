from django import forms
from .models import SocietyBoard

class BoardForm(forms.ModelForm):
    class Meta:
        model = SocietyBoard
        fields = ['writer', 'body']