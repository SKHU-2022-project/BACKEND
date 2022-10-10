from django.shortcuts import render
from .models import Question, Developer, Choice
from .serializers import DeveloperSerializer , QuestionSerializer , ChoiceSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
@api_view(['GET'])
def index(request):
    developers = Developer.objects.all()
    serializer = DeveloperSerializer(developers, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def form(request):
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def result(request): 
    # 문항 수
    N = Question.objects.count()
    # 개발자 유형 수
    K = Developer.objects.count()
    # 개발유형마다 몇 개인지 저장할 리스트 counter[1] = (1번 유형 점수(개수))
    counter = [0] * (K + 1)  
    for n in range(1, N+1):
        developer_id = int(request.POST[f'question-{n}'][0])
        counter[developer_id] += 1
    # 최고점 개발 유형
    best_developer_id = max(range(1, K + 1), key=lambda id: counter[id])
    best_developer = Developer.objects.get(pk=best_developer_id)
    best_developer.count += 1
    best_developer.save() 
    serializer = ChoiceSerializer( N,K,many=True)
    return Response(serializer.data)