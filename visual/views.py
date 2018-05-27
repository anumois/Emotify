from django.shortcuts import render
import requests
from . import visualLib
from . import serve
from .models import EmotifyTimeList

# Create your views here.
def index(request):
    TimeContext = []
    for ETL in EmotifyTimeList.objects.all():
        ETLTuple = str(ETL.ETLMonth) + "월 " + str(ETL.ETLDay) + "일"
        TimeContext.append(ETLTuple)
    context = {'TimeContext' : TimeContext}

    if request.method == 'GET':
        try:
            return display(request,[request.GET['indexLocation'],request.GET['indexLocation2']], [request.GET['CompindexLocation'], request.GET['CompindexLocation2']],request.GET['startTime'], request.GET['endTime'])
        except KeyError:
            return render(request, 'index.html', context)
    return render(request, 'index.html', context)

def display(request, location, complocation, startTime, endTime):
    TimeContext = []

    for ETL in EmotifyTimeList.objects.all():
        ETLTuple = str(ETL.ETLMonth) + "월 " + str(ETL.ETLDay) + "일"
        TimeContext.append(ETLTuple)


    if location[0] == complocation[0] and location[1] == complocation[1]:
        sOut = serve.serverOut(location,startTime,endTime)
        context = visualLib.monoregContext(location,sOut)
        context['TimeContext'] = TimeContext
        context['TimeQuery'] = startTime + ' ~ ' + endTime
        try:
            if context['result'] == 'success':
                return render(request, 'monodisplay.html', context)
            else:
                return notFound(request)
        except KeyError:
            return notFound(request)
    else:
        sOut = serve.serverOut(location, startTime, endTime)
        scompOut = serve.serverOut(complocation, startTime, endTime)

        context = visualLib.regContext(location, complocation, sOut, scompOut)
        context['TimeContext'] = TimeContext
        context['TimeQuery'] = startTime + ' ~ ' + endTime
        try:
            if context['result'] == 'success':
                return render(request, 'display.html', context)
            else:
                return notFound(request)
        except KeyError:
            return notFound(request)


def notFound(request):
    return render(request,'notFound.html')
