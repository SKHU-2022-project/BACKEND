from django import forms
from .models import HumanityBoard

class BoardForm(forms.ModelForm):
    class Meta:
        model = HumanityBoard
        fields = ['writer', 'body']