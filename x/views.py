from django.shortcuts import render
from .models import projects, c


def home(request):
    x = c.objects.all()
    return render(request, 'x/home.html', {'xs':x})

def proj(request):
    x = projects.objects.all()
    return render(request, 'x/projects.html', {'projects':x})