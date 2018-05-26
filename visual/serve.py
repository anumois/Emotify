from .models import EmotifyTimeList, EmotifyDictionary, EmotifyLocationList, EmotifyElement, EmotifyDictEntry
from .models import HappyEmotifyTweet, SadEmotifyTweet, SurpriseEmotifyTweet, AngerEmotifyTweet

from django.core.exceptions import ObjectDoesNotExist

import operator

#starting from 0th month - January - February - .... - December
DaysInMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def debugOut(locationData):
    debugContext = {'result':'success', 'Location': locationData, 'Happy':'50', 'Sad':'20', 'Surprise':'15', 'Anger': '15'}
    debugContext['HaKeyword'] = ['그뤠잇','좋아','굿 판단','고양이','강아지']
    debugContext['SaKeyword'] = ['허미','그래서','심장','잠와','뱀']
    debugContext['SuKeyword'] = ['깜놀','성냥개비','유튜브','끔찍','어이']
    debugContext['AnKeyword'] = ['환불','더미','정말','짜증나','고통']
    failContext = {'result':'fail', 'msg':'incorrect method'}
    return debugContext

def parseStartEnd(startTime, endTime):
    try:
        startMonthIndex = startTime.index('월')
        startDayIndex = startTime.index('일')
        endMonthIndex = endTime.index('월')
        endDayIndex = endTime.index('일')
        startMonth = int(startTime[0:startMonthIndex])
        startDay = int(startTime[startMonthIndex+1:startDayIndex])
        endMonth = int(endTime[0:endMonthIndex])
        endDay = int(endTime[endMonthIndex+1:endDayIndex])
    except ValueError:
        return [(0,0),(0,0)]

    try:
        startETL = EmotifyTimeList.objects.get(ETLMonth=startMonth, ETLDay = startDay)
        endETL = EmotifyTimeList.objects.get(ETLMonth=endMonth, ETLDay = endDay)
    except ObjectDoesNotExist:
        return [(0,0),(0,0)]

    if (startMonth > endMonth) or (startMonth == endMonth and startDay > endDay):
        return [(0,0),(0,0)]
    else:
        return [(startMonth,startDay), (endMonth,endDay)]

def getEE(curMonth, curDay, ELL):
    try:
        ETL = EmotifyTimeList.objects.get(ETLMonth=curMonth, ETLDay = curDay)
    except ObjectDoesNotExist:
        #print(str(curMonth) + " " + str(curDay) + 'No such ETL')
        return False

    try:
        EE = EmotifyElement.objects.get(EEDate = ETL, EELocation = ELL)
    except ObjectDoesNotExist:
        #print('No such EE')
        return False

    return EE

def serverOut(location, startTime, endTime):
    [(startMonth,startDay), (endMonth,endDay)] = parseStartEnd(startTime,endTime)
    (Location1, Location2) = location

    if startMonth == 0:
        return {'result':'failed', 'msg':'Invalid Date'}

    curMonth = startMonth
    curDay = startDay
    Happy = 0
    Sad = 0
    Surprise = 0
    Anger = 0
    HappyDict = {}
    SadDict = {}
    SurpriseDict = {}
    AngerDict = {}
    EmotionDict = [HappyDict, SadDict, SurpriseDict, AngerDict]
    HappyTweet = {}
    SadTweet = {}
    SurpriseTweet = {}
    AngerTweet = {}


    try:
        ELL = EmotifyLocationList.objects.get(ELLLocation1 = Location1, ELLLocation2 = Location2)
    except ObjectDoesNotExist:
        return {'result':'failed', 'msg':'Invalid Location'}

    while(True):
        EE = getEE(curMonth, curDay, ELL)

        if EE is not False:
            Happy = Happy + EE.EEHappy
            Sad = Sad + EE.EESad
            Surprise = Surprise + EE.EESurprise
            Anger = Anger + EE.EEAnger
            for DictElem in EmotifyDictionary.objects.filter(EDElement = EE):
                iteration = 0
                for DictEntry in EmotifyDictEntry.objects.filter(EDEContainer = DictElem).order_by('EDEValue').reverse():
                    if iteration == 10:
                        break
                    try:
                        EmotionDict[(DictElem.EDType)-1][DictEntry.EDEKey] = EmotionDict[(DictElem.EDType)-1][DictEntry.EDEKey] + DictEntry.EDEValue
                    except KeyError:
                        EmotionDict[(DictElem.EDType)-1][DictEntry.EDEKey] = DictEntry.EDEValue

                    iteration = iteration + 1

        else:
            pass

        if curMonth == endMonth and curDay == endDay:
            break

        if curDay == DaysInMonth[curMonth] and curMonth is not 12:
            curMonth = curMonth + 1
            curDay = 1
        elif curDay == DaysInMonth[curMonth] and curMonth == 12:
            curMonth = 1
            curDay = 1
        else:
            curDay = curDay + 1


    sortedHappy = sorted(HappyDict.items(), key=operator.itemgetter(1), reverse=True)[0:15]
    sortedSad = sorted(SadDict.items(), key=operator.itemgetter(1), reverse=True)[0:5]
    sortedSurprise = sorted(SurpriseDict.items(), key=operator.itemgetter(1), reverse=True)[0:15]
    sortedAnger = sorted(AngerDict.items(), key=operator.itemgetter(1), reverse=True)[0:15]

    sortedHaTweet = {}
    sortedSaTweet = {}
    sortedSuTweet = {}
    sortedAnTweet = {}



    iteration = 0
    for values in sortedHappy:
        ETList = HappyEmotifyTweet.objects.filter(ETContainer = ELL, ETKey = values[0]).order_by('?')
        innerIter = 0
        for ET in ETList:
            try:
                sortedHaTweet[values[0]].append(ET.ETText+ '\n')
            except KeyError:
                sortedHaTweet[values[0]] = [ET.ETText+ '\n']
                iteration = iteration + 1
            innerIter = innerIter + 1
            if innerIter > 5:
                break

        if iteration > 4:
            break

    iteration = 0
    for values in sortedSad:
        ETList = SadEmotifyTweet.objects.filter(ETContainer = ELL, ETKey = values[0]).order_by('?')
        innerIter = 0
        for ET in ETList:
            try:
                sortedSaTweet[values[0]].append(ET.ETText+ '\n')
            except KeyError:
                sortedSaTweet[values[0]] = [ET.ETText+ '\n']
                iteration = iteration + 1
            innerIter = innerIter + 1
            if innerIter > 5:
                break
        if iteration > 4:
            break
    iteration = 0
    for values in sortedSurprise:
        ETList = SurpriseEmotifyTweet.objects.filter(ETContainer = ELL, ETKey = values[0]).order_by('?')
        innerIter = 0
        for ET in ETList:
            try:
                sortedSuTweet[values[0]].append(ET.ETText + '\n')
            except KeyError:
                sortedSuTweet[values[0]] = [ET.ETText + '\n']
                iteration = iteration + 1
            innerIter = innerIter + 1
            if innerIter > 5:
                break
        if iteration > 4:
            break
    iteration = 0
    for values in sortedAnger:
        ETList = AngerEmotifyTweet.objects.filter(ETContainer = ELL, ETKey = values[0]).order_by('?')
        innerIter = 0
        for ET in ETList:
            try:
                sortedAnTweet[values[0]].append(ET.ETText + '\n')
            except KeyError:
                sortedAnTweet[values[0]] = [ET.ETText + '\n']
                iteration = iteration + 1
            innerIter = innerIter + 1
            if innerIter > 5:
                break
        if iteration > 4:
            break


    context = {'result':'success'}
    context['Happy'] = Happy
    context['Sad'] = Sad
    context['Surprise'] = Surprise
    context['Anger'] = Anger

    context['HaKeyword'] = sortedHappy
    context['SaKeyword'] = sortedSad
    context['SuKeyword'] = sortedSurprise
    context['AnKeyword'] = sortedAnger

    context['HaTweet'] = sortedHaTweet
    context['SaTweet'] = sortedSaTweet
    context['SuTweet'] = sortedSuTweet
    context['AnTweet'] = sortedAnTweet

    return context
