def debugOut(locationData):
    debugContext = {'result':'success', 'Location': locationData, 'Happy':'50', 'Sad':'20', 'Surprise':'15', 'Anger': '15'}
    debugContext['HaKeyword'] = ['그뤠잇','좋아','굿 판단','고양이','강아지']
    debugContext['SaKeyword'] = ['허미','그래서','심장','잠와','뱀']
    debugContext['SuKeyword'] = ['깜놀','성냥개비','유튜브','끔찍','어이']
    debugContext['AnKeyword'] = ['환불','더미','정말','짜증나','고통']
    failContext = {'result':'fail', 'msg':'incorrect method'}
    return debugContext

def serverOut(locationData):
    return debugOut(locationData)
