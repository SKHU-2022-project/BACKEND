from django import forms
from .models import MediaContentBoard

class BoardForm(forms.ModelForm):
    class Meta:
        model =  MediaContentBoard
        fields = ['writer', 'body']