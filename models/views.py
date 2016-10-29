from django.shortcuts import render
from django.template import RequestContext
from .models import data_locality

def BeersAll(request):
        beers = data_locality.objects.all().order_by('name')
        #beers = Beer.description.maketrans().order_by('name')
        context = {'data': data_locality}
        return render(request, 'beersall.html', context)
        return render(request, 'beersall.html', context)
        return render(request, 'beersall.html', context)