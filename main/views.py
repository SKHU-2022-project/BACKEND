from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import ITBoardForm, SocietyBoardForm, HumanityBoardForm, MediaContentBoardForm
from .models import ITBoard, HumanityBoard, SocietyBoard, MediaContentBoard

# Create your views here.
def main(request):
    return render(request, 'main.html')

def itboard(request):
    writings = ITBoard.objects.all()
    form = ITBoardForm()
    if request.method == 'POST':
        form = ITBoardForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.date = timezone.now()
            form.save()
            return redirect('itBoard')
    else:
        return render(request, 'itboard.html', {'form':form, 'writings':writings})
    

def societyBoard(request):
    writings = SocietyBoard.objects.all()
    form = SocietyBoardForm()
    if request.method == 'POST':
        form = SocietyBoardForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.date = timezone.now()
            form.save()
            return redirect('societyBoard')
    else:
        return render(request, 'societyBoard.html', {'form':form, 'writings':writings})

def mediacontentBoard(request):
    writings = MediaContentBoard.objects.all()
    form = MediaContentBoardForm()
    if request.method == 'POST':
        form = MediaContentBoardForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.date = timezone.now()
            form.save()
            return redirect('mediacontentBoard')
    else:
        return render(request, 'mediacontentboard.html', {'form':form, 'writings':writings})
    
def humanityBoard(request):
    writings = HumanityBoard.objects.all()
    form = HumanityBoardForm()
    if request.method == 'POST':
        form = HumanityBoardForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.date = timezone.now()
            form.save()
            return redirect('humanityBoard')
    else:
        return render(request, 'humanityboard.html', {'form':form, 'writings':writings}) 