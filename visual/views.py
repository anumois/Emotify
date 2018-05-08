from django.shortcuts import render
import requests
from . import visualLib

# Create your views here.
def index(request):
    if request.method == 'POST':
        try:
            pass
        except KeyError:
            return render(request, 'index.html')
    return render(request, 'index.html')

def display(request):
    r = requests.get('http://127.0.0.1:8000/api/getInfo')
    jsonResult = r.json()
    context = visualLib.copyJson2Context(jsonResult)

    if context['result'] != False:
        return render(request, 'display.html', context)
    else:
        return notFound(request)

def notFound(request):
    return render(request,'notFound.html')
