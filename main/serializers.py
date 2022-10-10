import imp
from rest_framework import serializers
from .models import Developer, Question , Choice

class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = ('name', 'count') #라우팅을 시리얼라이즈에서 도와줌을로 서 API구현을 쉽게 해준다.

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('number' , 'content')

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        field = ('content','question' ,'developer')