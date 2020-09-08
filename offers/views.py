from django.shortcuts import render,get_object_or_404
from offers.models import OffersAd
from django.core.paginator import Paginator
from offers.filters import OffersFilter


def homepage(request):
    posts = OffersAd.objects.all()

    myfilter = OffersFilter(request.GET, queryset=posts)
    posts = myfilter.qs
    
    
    paginator = Paginator(posts,10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    context = {
        'posts':posts,
        'myfilter':myfilter,
        
    }

    return render(request,'offers/home.html',context)

def offer_detail(request, slug):
    context = {}
    offer_detail = get_object_or_404(OffersAd, slug=slug)
    context['offer_detail'] = offer_detail
    return render(request, 'offers/offer_detail.html', context)