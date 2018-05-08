from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def debugOut(request):
    debugContext = {'result':'success', 'Location': '전국', 'Happy':'50', 'Sad':'20', 'Surprise':'15', 'Anger': '15'}
    failContext = {'result':'fail', 'msg':'incorrect method'}
    if request.method == 'GET':
        return JsonResponse(debugContext)
    else:
        return JsonResponse(failContext)
