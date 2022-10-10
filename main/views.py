from django.shortcuts import render
from .models import IT, ITAnswer, ITQuestion
from .serializers import ITSerializer , ITQuestionSerializer , ITAnswerSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
@api_view(['GET'])
def index(request):
    majors = IT.objects.all()
    serializer = ITSerializer(majors, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def form(request):
    questions = ITQuestion.objects.all()
    serializer = ITQuestionSerializer(questions, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def submit(request): 
    # 문항 수
    N = ITQuestion.objects.count()
    # 개발자 유형 수
    K = IT.objects.count()
    # 개발유형마다 몇 개인지 저장할 리스트 counter[1] = (1번 유형 점수(개수))
    counter = [0] * (K + 1)  
    for n in range(1, N+1):
        major_id = int(request.POST[f'question-{n}'][0])
        counter[major_id] += 1
    # 최고점 개발 유형
    best_major_id = max(range(1, K + 1), key=lambda id: counter[id])
    best_major_id = IT.objects.get(pk=best_major_id)
    best_major_id.count += 1
    best_major_id.save()
    
    major_id = best_major_id
    serializer = ITSerializer(major_id)
    #serializer = ChoiceSerializer(N,K,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def result(request, major_id):
    major = IT.objects.get(id=major_id)
    serialize = ITSerializer(major, many=False)
    return Response(serialize.data)