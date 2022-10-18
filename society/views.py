from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import BoardForm
from .models import Society, Society_CN, Society_ENG, SocietyBoard, SocietyQuestion, SocietyAnswer
from .models import SocietyAnswer_ENG, SocietyQuestion_ENG, SocietyQuestion_CN, SocietyAnswer_CN
# Create your views here.
def societyTest(request):
    questions =SocietyQuestion.objects.all()
    
    return render(request, 'test.html', {'questions':questions})

def societySubmit(request):
    N = SocietyQuestion.objects.count()
    K = Society.objects.count()

    counter = [0] * (K + 1)
        
    for n in range(1, N+1):
        major_id = int(request.POST[f'question-{n}'][0])
        counter[major_id] += 1
        
    max_value = max(counter)
    best_major_id = counter.index(max_value)
    best_major = Society.objects.get(pk=best_major_id)
    best_major.count += 1
    best_major.save()
    
    context = {
        'major' : best_major,
        'counter' : counter
    }
    
    return redirect('result', major_id=best_major_id)

def societyResult(request, major_id):
    major = Society.objects.get(pk=major_id)
    return render(request, 'result.html', {'major':major})


def societyEngTest(request):
    questions = SocietyQuestion_ENG.objects.all()
    
    return render(request, 'engtest.html', {'questions':questions})

def societyEngSubmit(request):
    N = SocietyQuestion_ENG.objects.count()
    K = Society_ENG.objects.count()

    counter = [0] * (K + 1)
        
    for n in range(1, N+1):
        major_id = int(request.POST[f'question-{n}'][0])
        counter[major_id] += 1
        
    max_value = max(counter)
    best_major_id = counter.index(max_value)
    best_major = Society_ENG.objects.get(pk=best_major_id)
    best_major.count += 1
    best_major.save()
    
    context = {
        'major' : best_major,
        'counter' : counter
    }
    
    return redirect('engresult', major_id=best_major_id)

def societyEngResult(request, major_id):
    major = Society_ENG.objects.get(pk=major_id)
    return render(request, 'engresult.html', {'major':major})

def societyCnTest(request):
    questions = SocietyQuestion_CN.objects.all()
    
    return render(request, 'engtest.html', {'questions':questions})

def societyCnSubmit(request):
    N = SocietyQuestion_CN.objects.count()
    K = Society_CN.objects.count()

    counter = [0] * (K + 1)
        
    for n in range(1, N+1):
        major_id = int(request.POST[f'question-{n}'][0])
        counter[major_id] += 1
        
    max_value = max(counter)
    best_major_id = counter.index(max_value)
    best_major = Society_CN.objects.get(pk=best_major_id)
    best_major.count += 1
    best_major.save()
    
    context = {
        'major' : best_major,
        'counter' : counter
    }
    
    return redirect('cnresult', major_id=best_major_id)

def societyCnResult(request, major_id):
    major = Society_CN.objects.get(pk=major_id)
    return render(request, 'cnresult.html', {'major':major})

def societyBoard(request):
    writings = SocietyBoard.objects.all()
    form = BoardForm()
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.date = timezone.now()
            form.save()
            return redirect('societyBoard')
    else:
        return render(request, 'societyBoard.html', {'form':form, 'writings':writings})
