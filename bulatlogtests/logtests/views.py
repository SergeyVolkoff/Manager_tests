from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify


menu = ['About tests', 'Result']

data_db = [
    {'id':1,'title':'test OSPF', 'content':'result test OSPF','is_published': True},
    {'id':2,'title':'test rip', 'content':'result test RIP','is_published':True},
    {'id':3,'title':'test bgp', 'content':'result test BGP','is_published':True},
    ]

def index(request):
    # return HttpResponse("<h1>TESTS SUITE LOG</h1>")
    data= {
        'title': 'TESTS SUITE LOG',
        'menu': menu,
        'suite_test':data_db
    }
    return render(request,'logtests/index.html',context = data)

def statistic_testing(request,stat_id):
    return HttpResponse(f"Test Statistics<p>id: {stat_id}</p>")

def statistic_by_slug(request, stat_slug):
    return HttpResponse(f"Test Statistics<p>slug: {stat_slug}</p>")

def show_test_data(request,test_data_id):
    return HttpResponse(f"View data test id={test_data_id}")

def page_not_found(request, exception):
    return HttpResponse("<h1>No test page</h1>")