from django.shortcuts import render

def portfolio(request):
    return render(request, 'portfolio/portfolio.html')

def project(request):
    return render(request, 'portfolio/project.html')