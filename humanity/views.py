from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import BoardForm
from .models import Humanity, Humanity_CN, Humanity_ENG, HumanityBoard, HumanityQuestion, HumanityAnswer
from .models import HumanityAnswer_ENG, HumanityQuestion_ENG, HumanityQuestion_CN, HumanityAnswer_CN
# Create your views here.
def humanityTest(request):
    questions =HumanityQuestion.objects.all()
    
    return render(request, 'test.html', {'questions':questions})

def humanitySubmit(request):
    N = HumanityQuestion.objects.count()
    K = Humanity.objects.count()

    counter = [0] * (K + 1)
        
    for n in range(1, N+1):
        major_id = int(request.POST[f'question-{n}'][0])
        counter[major_id] += 1
        
    max_value = max(counter)
    best_major_id = counter.index(max_value)
    best_major = Humanity.objects.get(pk=best_major_id)
    best_major.count += 1
    best_major.save()
    
    context = {
        'major' : best_major,
        'counter' : counter
    }
    
    return redirect('result', major_id=best_major_id)

def humanityResult(request, major_id):
    major = Humanity.objects.get(pk=major_id)
    return render(request, 'result.html', {'major':major})


def humanityEngTest(request):
    questions =HumanityQuestion_ENG.objects.all()
    
    return render(request, 'engtest.html', {'questions':questions})

def humanityEngSubmit(request):
    N = HumanityQuestion_ENG.objects.count()
    K = Humanity_ENG.objects.count()

    counter = [0] * (K + 1)
        
    for n in range(1, N+1):
        major_id = int(request.POST[f'question-{n}'][0])
        counter[major_id] += 1
        
    max_value = max(counter)
    best_major_id = counter.index(max_value)
    best_major = Humanity_ENG.objects.get(pk=best_major_id)
    best_major.count += 1
    best_major.save()
    
    context = {
        'major' : best_major,
        'counter' : counter
    }
    
    return redirect('engresult', major_id=best_major_id)

def humanityEngResult(request, major_id):
    major = Humanity.objects.get(pk=major_id)
    return render(request, 'engresult.html', {'major':major})

def humanityCnTest(request):
    questions =HumanityQuestion_CN.objects.all()
    
    return render(request, 'engtest.html', {'questions':questions})

def humanityCnSubmit(request):
    N = HumanityQuestion_CN.objects.count()
    K = Humanity_CN.objects.count()

    counter = [0] * (K + 1)
        
    for n in range(1, N+1):
        major_id = int(request.POST[f'question-{n}'][0])
        counter[major_id] += 1
        
    max_value = max(counter)
    best_major_id = counter.index(max_value)
    best_major = Humanity_CN.objects.get(pk=best_major_id)
    best_major.count += 1
    best_major.save()
    
    context = {
        'major' : best_major,
        'counter' : counter
    }
    
    return redirect('cnresult', major_id=best_major_id)

def humanityCnResult(request, major_id):
    major = Humanity_CN.objects.get(pk=major_id)
    return render(request, 'cnresult.html', {'major':major})

def humanityBoard(request):
    writings = HumanityBoard.objects.all()
    form = BoardForm()
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.date = timezone.now()
            form.save()
            return redirect('itBoard')
    else:
        return render(request, 'humanityboard.html', {'form':form, 'writings':writings})
