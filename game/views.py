from django.shortcuts import render
from .models import Level
from django.http import Http404

def index(request):
    return render(request , 'game/index.html', {'levels' : Level.objects.all()})

def show(request , id):
    try:
        level = Level.objects.get(id=id)
    except Level.DoesNotExist:
        raise Http404(id)
    return render(request , 'game/level.html', { 'level' : level})
