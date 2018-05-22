def regContext(location, complocation, sOut, scompOut):
    context = {'result': 'success'}

    try:
        sHappy = sOut['Happy']
        sSad = sOut['Sad']
        sSurprise = sOut['Surprise']
        sAnger = sOut['Anger']
        sumEmo = sHappy + sSad + sSurprise + sAnger

        scompHappy = scompOut['Happy']
        scompSad = scompOut['Sad']
        scompSurprise = scompOut['Surprise']
        scompAnger = scompOut['Anger']
        compsumEmo = scompHappy + scompSad + scompSurprise + scompAnger

        if sumEmo != 0:
            sHappy = int((float(sHappy) / float(sumEmo)) * 100)
            sSad = int((float(sSad) / float(sumEmo)) * 100)
            sSurprise = int((float(sSurprise) / float(sumEmo)) * 100)
            sAnger = int((float(sAnger) / float(sumEmo)) * 100)
        if compsumEmo != 0:
            scompHappy = int((float(scompHappy) / float(compsumEmo)) * 100)
            scompSad = int((float(scompSad) / float(compsumEmo)) * 100)
            scompSurprise = int((float(scompSurprise) / float(compsumEmo)) * 100)
            scompAnger = int((float(scompAnger) / float(compsumEmo)) * 100)

        context['sHappy'] = sHappy
        context['sSad'] = sSad
        context['sSurprise'] = sSurprise
        context['sAnger'] = sAnger


        context['sHaKeyword'] = []
        for member in sOut['HaKeyword']:
            context['sHaKeyword'].append([member[0],sOut['HaTweet'][member[0]]])
        context['sSaKeyword'] = []
        for member in sOut['SaKeyword']:
            context['sSaKeyword'].append([member[0],sOut['SaTweet'][member[0]]])
        context['sSuKeyword'] = []
        for member in sOut['SuKeyword']:
            context['sSuKeyword'].append([member[0],sOut['SuTweet'][member[0]]])
        context['sAnKeyword'] = []
        for member in sOut['AnKeyword']:
            context['sAnKeyword'].append([member[0],sOut['AnTweet'][member[0]]])

        context['scompHappy'] = scompHappy
        context['scompSad'] = scompSad
        context['scompSurprise'] = scompSurprise
        context['scompAnger'] = scompAnger

        context['scompHaKeyword'] = []
        for member in scompOut['HaKeyword']:
            context['scompHaKeyword'].append([member[0],scompOut['HaTweet'][member[0]]])
        context['scompSaKeyword'] = []
        for member in scompOut['SaKeyword']:
            context['scompSaKeyword'].append([member[0],scompOut['SaTweet'][member[0]]])
        context['scompSuKeyword'] = []
        for member in scompOut['SuKeyword']:
            context['scompSuKeyword'].append([member[0],scompOut['SuTweet'][member[0]]])
        context['scompAnKeyword'] = []
        for member in scompOut['AnKeyword']:
            context['scompAnKeyword'].append([member[0],scompOut['AnTweet'][member[0]]])

        context['sLocation1'] = location[0]
        context['sLocation2'] = location[1]

        context['scompLocation1'] = complocation[0]
        context['scompLocation2'] = complocation[1]
        return context

    except KeyError:
        return False
