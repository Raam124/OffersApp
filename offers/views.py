from django.shortcuts import render,get_object_or_404
from offers.models import OffersAd
from django.core.paginator import Paginator
from offers.filters import OffersFilter


from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from offers.serializers import OffersSerializer
from rest_framework.decorators import api_view,renderer_classes
from rest_framework.response import Response
from rest_framework import viewsets





def homepage(request):
    posts = OffersAd.objects.all().order_by("-date_published")

    myfilter = OffersFilter(request.GET, queryset=posts)
    posts = myfilter.qs
    
   
    paginator = Paginator(posts,21)
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


def aboutus(request):
    return render(request,'offers/aboutus.html')


def landing_page(request):
    return render(request,'offers/landing_page.html')



@api_view(['GET'])
def offers_list(request):
        snippets = OffersAd.objects.all()
        serializer = OffersSerializer(snippets, many=True)
        return Response(serializer.data)


