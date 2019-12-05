from django.shortcuts import render
from .models import Level
from .models import World
from .models import Detail
from django.http import Http404

def index(request):
    return render(request , 'game/index.html', {'levels' : Level.objects.all()})

def show(request , id):
    try:
        level = Level.objects.get(id=id)
        detail = Detail.objects.filter(id_level = id)
    except Level.DoesNotExist:
        raise Http404(id)
    return render(request , 'game/level.html', { 'level' : level, 'detail' : detail})

def form_user(request):
    return render(request , 'game/form_user.html')
