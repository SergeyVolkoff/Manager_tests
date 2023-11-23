from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify


menu = [
    {'title':'REPORT','url_name':'report'},
    {'title':'LOG','url_name':'log'},
]

data_db = [
    {'id':1,'title':'TotalStatistic', 'content':'TotalPassFail dfdfgd fbbfdb dbdfbdfb xcvxcvsrxfb dbffb','is_published': True},
    {'id':2,'title':'Satistic by Suite', 'content':'TotalPassFail','is_published':True},
    {'id':3,'title':'Statistic by tag', 'content':'TotalPassFail','is_published':True},
    ]

def index(request):
    # return HttpResponse("<h1>Test Statistics</h1>")
    data= {
        'menu': menu,
        'title': 'Test Statistics',
        'suite_test':data_db
    }
    return render(request,'logtests/index.html',context = data)

def show_test_detail(request,test_data_id):
    return HttpResponse(f"Test detail Log id={test_data_id}")

def log(request):
    return  render(
        request,
        'logtests/log.html',
        {'title': 'LOG','menu': menu,}
    )
        
def report(request):
    return render(
        request,
        'logtests/report.html',
        {'title': 'REPORT','menu': menu,}
        )

def test_execution_log(request):
    return HttpResponse()

def page_not_found(request, exception):
    return HttpResponse("<h1>No test page</h1>")