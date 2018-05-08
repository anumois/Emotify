from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def debugOut(request):
    debugContext = {'result':'success', 'Location': '전국', 'Happy':'50', 'Sad':'20', 'Surprise':'15', 'Anger': '15'}
    debugContext['HaKeyword'] = ['그뤠잇','좋아','굿 판단','고양이','강아지']
    debugContext['SaKeyword'] = ['허미','그래서','심장','잠와','뱀']
    debugContext['SuKeyword'] = ['깜놀','성냥개비','유튜브','끔찍','어이']
    debugContext['AnKeyword'] = ['환불','더미','정말','짜증나','고통']
    failContext = {'result':'fail', 'msg':'incorrect method'}
    if request.method == 'GET':
        return JsonResponse(debugContext)
    else:
        return JsonResponse(failContext)
