from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def portfolio_single(request):
    return render(request, 'portfolio-single.html')

def team(request):
    return render(request, 'team.html')