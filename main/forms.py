from django import forms
from .models import ITBoard, HumanityBoard, MediaContentBoard, SocietyBoard

class ITBoardForm(forms.ModelForm):
    class Meta:
        model = ITBoard
        fields = ['writer', 'body']

class HumanityBoardForm(forms.ModelForm):
    class Meta:
        model = HumanityBoard
        fields = ['writer', 'body']

class MediaContentBoardForm(forms.ModelForm):
    class Meta:
        model =  MediaContentBoard
        fields = ['writer', 'body']

class SocietyBoardForm(forms.ModelForm):
    class Meta:
        model = SocietyBoard
        fields = ['writer', 'body']