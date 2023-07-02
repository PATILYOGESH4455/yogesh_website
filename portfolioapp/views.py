from django.shortcuts import render
from .models import Project

# Create your views here.

def homePage(request):
    projects = Project.objects.all()
    for i in projects:
        print(i)
        context = {'projects': projects}

    return render(request, 'base/index.html', context)

def aboutPage(request):
    return render(request, 'base/about.html')

# def resume(request):



