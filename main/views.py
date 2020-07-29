from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import project_upload

# Create your views here.

def index(request):
    obj = project_upload.objects.all()
    return render(request, 'index.html', {'obj':obj})

def portfolio(request):
    obj = project_upload.objects.all()
    return render(request, 'portfolio.html', {'obj':obj})

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def portfolio_single(request, pk):
    obj = get_object_or_404(project_upload, pk=pk)
    return render(request, 'portfolio-single.html', {'obj':obj})

def team(request):
    return render(request, 'team.html')
