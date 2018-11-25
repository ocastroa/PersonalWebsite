from django.shortcuts import get_object_or_404, render
from .models import Portfolio
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def index(request):
    portfolio = Portfolio.objects.order_by('-app_id').filter(is_published=True) # order by date
    paginator = Paginator(portfolio,6)
    page = request.GET.get('page')
    paged_portfolio = paginator.get_page(page)

    context = {
        'portfolio': paged_portfolio
    }
    return render(request, 'portfolio/portfolio.html', context)

def project(request,slug):
    project = get_object_or_404(Portfolio, slug=slug)
    context = {
        'project': project
    }
    return render(request, 'portfolio/project.html', context)