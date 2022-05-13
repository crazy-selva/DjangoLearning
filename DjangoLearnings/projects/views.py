from django.shortcuts import render
from django.http import HttpResponse

def projects(request):
    return render(request, 'projects/projects.html')

def project(request,id):
    return render(request, 'projects/single-project.html')

def pro(reques):
    return HttpResponse("fuckoff")