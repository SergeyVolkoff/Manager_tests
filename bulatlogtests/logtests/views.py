from django.http import HttpResponse
from django.shortcuts import render

menu = ['About tests', 'Result']


def index(request):
    # return HttpResponse("<h1>TESTS SUITE LOG</h1>")
    data= {
        'title': 'TESTS SUITE LOG',
        'menu': menu,
    }
    return render(request,'logtests/index.html',context = data)

def statistic_testing(request,stat_id):
    return HttpResponse(f"Test Statistics<p>id: {stat_id}</p>")

def statistic_by_slug(request, stat_slug):
    return HttpResponse(f"Test Statistics<p>slug: {stat_slug}</p>")