from django.shortcuts import render
from pages.models import Pages

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    oscars_pic = Pages.objects.all().filter(name='Oscar')
    context = {
        'oscars_pic': oscars_pic
    }
    return render(request, 'pages/about.html', context)