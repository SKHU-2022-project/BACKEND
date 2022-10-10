import imp
from rest_framework import serializers
from .models import IT, ITQuestion, ITAnswer

class ITSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT
        fields = ('major', 'count') #라우팅을 시리얼라이즈에서 도와줌을로 서 API구현을 쉽게 해준다.

class ITQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ITQuestion
        fields = ('number' , 'question')

class ITAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ITAnswer
        field = ('answer','question' ,'major')