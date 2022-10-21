from django.shortcuts import render, redirect
from django.utils import timezone
from .models import IT, IT_ch, IT_eng, ITAnswer, ITAnswer_ch, ITAnswer_eng
from .models import ITQuestion, ITQuestion_ch, ITQuestion_eng
# Create your views here.
def itTest(request):
    questions =ITQuestion.objects.all()
    
    return render(request, 'test.html', {'questions':questions})

def itSubmit(request):
    N = ITQuestion.objects.count()
    K = IT.objects.count()

    counter = [0] * (K + 1)
        
    for n in range(1, N+1):
        major_id = int(request.POST[f'question-{n}'][0])
        counter[major_id] += 1
        
    max_value = max(counter)
    best_major_id = counter.index(max_value)
    best_major = IT.objects.get(pk=best_major_id)
    best_major.count += 1
    best_major.save()
    
    context = {
        'major' : best_major,
        'counter' : counter
    }
    
    return redirect('result', major_id=best_major_id)

def itResult(request, major_id):
    major = IT.objects.get(pk=major_id)
    return render(request, 'result.html', {'major':major})


def itEngTest(request):
    questions =ITQuestion_eng.objects.all()
    
    return render(request, 'test.html', {'questions':questions})

def itEngSubmit(request):
    N = ITQuestion_eng.objects.count()
    K = IT_eng.objects.count()

    counter = [0] * (K + 1)
        
    for n in range(1, N+1):
        major_id = int(request.POST[f'question-{n}'][0])
        counter[major_id] += 1
        
    max_value = max(counter)
    best_major_id = counter.index(max_value)
    best_major = IT_eng.objects.get(pk=best_major_id)
    best_major.count += 1
    best_major.save()
    
    context = {
        'major' : best_major,
        'counter' : counter
    }
    
    return redirect('result', major_id=best_major_id)

def itEngResult(request, major_id):
    major = IT.objects.get(pk=major_id)
    return render(request, 'itengresult.html', {'major':major})

def itChTest(request):
    questions =ITQuestion_ch.objects.all()
    
    return render(request, 'chittest.html', {'questions':questions})

def itChSubmit(request):
    N = ITQuestion_ch.objects.count()
    K = IT_ch.objects.count()

    counter = [0] * (K + 1)
        
    for n in range(1, N+1):
        major_id = int(request.POST[f'question-{n}'][0])
        counter[major_id] += 1
        
    max_value = max(counter)
    best_major_id = counter.index(max_value)
    best_major = IT_ch.objects.get(pk=best_major_id)
    best_major.count += 1
    best_major.save()
    
    context = {
        'major' : best_major,
        'counter' : counter
    }
    
    return redirect('chitresult', major_id=best_major_id)

def itChResult(request, major_id):
    major = IT_ch.objects.get(pk=major_id)
    return render(request, 'itchresult.html', {'major':major})

