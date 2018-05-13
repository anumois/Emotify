from django.shortcuts import render
import requests
from . import visualLib
from . import serve
# Create your views here.
def index(request):
    if request.method == 'GET':
        try:
            return display(request,request.GET['indexLocation'])
        except KeyError:
            return render(request, 'index.html')
    return render(request, 'index.html')

def display(request, indexLocation):
    jsonResult = serve.serverOut(indexLocation)
    context = visualLib.copyJson2Context(jsonResult)

    if context['result'] != False:
        return render(request, 'display.html', context)
    else:
        return notFound(request)

def notFound(request):
    return render(request,'notFound.html')
