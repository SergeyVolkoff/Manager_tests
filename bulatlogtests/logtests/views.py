from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<h1>TESTS SUITE LOG</h1>")

def statistic_testing(request,stat_id):
    return HttpResponse(f"Test Statistics<p>id: {stat_id}</p>")

def statistic_by_slug(request, stat_slug):
    return HttpResponse(f"Test Statistics<p>slug: {stat_slug}</p>")