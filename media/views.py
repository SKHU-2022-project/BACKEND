from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import BoardForm
from .models import MediaContent, MediaContent_CN, MediaContent_ENG, MediaContentBoard, MediaContentQuestion, HumanityAnswer
from .models import MediaContentAnswer_ENG, MediaContentQuestion_ENG, MediaContentQuestion_CN, MediaContentAnswer_CN
# Create your views here.
def mediacontentTest(request):
    questions =MediaContentQuestion.objects.all()
    
    return render(request, 'test.html', {'questions':questions})

def mediacontentSubmit(request):
    N = MediaContentQuestion.objects.count()
    K = MediaContent.objects.count()

    counter = [0] * (K + 1)
        
    for n in range(1, N+1):
        major_id = int(request.POST[f'question-{n}'][0])
        counter[major_id] += 1
        
    max_value = max(counter)
    best_major_id = counter.index(max_value)
    best_major = MediaContent.objects.get(pk=best_major_id)
    best_major.count += 1
    best_major.save()
    
    context = {
        'major' : best_major,
        'counter' : counter
    }
    
    return redirect('result', major_id=best_major_id)

def mediacontentResult(request, major_id):
    major = MediaContent.objects.get(pk=major_id)
    return render(request, 'result.html', {'major':major})


def mediacontentEngTest(request):
    questions = MediaContentQuestion_ENG.objects.all()
    
    return render(request, 'engtest.html', {'questions':questions})

def mediacontentEngSubmit(request):
    N = MediaContentQuestion_ENG.objects.count()
    K = MediaContent_ENG.objects.count()

    counter = [0] * (K + 1)
        
    for n in range(1, N+1):
        major_id = int(request.POST[f'question-{n}'][0])
        counter[major_id] += 1
        
    max_value = max(counter)
    best_major_id = counter.index(max_value)
    best_major = MediaContent_ENG.objects.get(pk=best_major_id)
    best_major.count += 1
    best_major.save()
    
    context = {
        'major' : best_major,
        'counter' : counter
    }
    
    return redirect('engresult', major_id=best_major_id)

def mediacontentEngResult(request, major_id):
    major = MediaContent_ENG.objects.get(pk=major_id)
    return render(request, 'engresult.html', {'major':major})

def mediacontentCnTest(request):
    questions = MediaContentQuestion_CN.objects.all()
    
    return render(request, 'engtest.html', {'questions':questions})

def mediacontentCnSubmit(request):
    N = MediaContentQuestion_CN.objects.count()
    K = MediaContent_CN.objects.count()

    counter = [0] * (K + 1)
        
    for n in range(1, N+1):
        major_id = int(request.POST[f'question-{n}'][0])
        counter[major_id] += 1
        
    max_value = max(counter)
    best_major_id = counter.index(max_value)
    best_major = MediaContent_CN.objects.get(pk=best_major_id)
    best_major.count += 1
    best_major.save()
    
    context = {
        'major' : best_major,
        'counter' : counter
    }
    
    return redirect('cnresult', major_id=best_major_id)

def mediacontentCnResult(request, major_id):
    major = MediaContent_CN.objects.get(pk=major_id)
    return render(request, 'cnresult.html', {'major':major})

def mediacontentBoard(request):
    writings = MediaContentBoard.objects.all()
    form = BoardForm()
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.date = timezone.now()
            form.save()
            return redirect('mediacontentBoard')
    else:
        return render(request, 'mediacontentboard.html', {'form':form, 'writings':writings})
