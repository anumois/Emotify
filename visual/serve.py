from .models import EmotifyTimeList, EmotifyDictionary, EmotifyLocationList, EmotifyElement, EmotifyDictEntry

from django.core.exceptions import ObjectDoesNotExist

import operator

Kangwon = ['강원', '도지사', '강릉', '고성', '동해', '삼척', '속초', '양구', '양양', '영월', '원주', '인제', '정선', '철원', '춘천', '태백', '평창', '홍천', '화천', '횡성']
Kyunggi = ['경기', '도지사', '가평', '고양', '과천', '광명', '광주', '구리', '군포', '김포', '남양주', '동두천', '부천', '성남', '수원', '시흥', '안산', '안성', '안양', '양주', '양평', '여주', '연천', '오산', '용인', '의왕', '의정부', '이천', '파주', '평택', '포천', '하남', '화성']
Kyungnam = ['경남','도지사', '거제', '거창', '고성', '김해', '남해', '밀양', '사천', '산청', '양산', '의령', '진주', '창녕', '창원', '통영', '하동', '함안', '함양', '합천']
Kyungbuk = ['경북', '도지사', '경산', '경주', '고령', '구미', '군위', '김천', '문경', '봉화', '상주', '성주', '안동', '영덕', '영양', '영주', '영천', '예천', '울릉', '울진', '의성', '청도', '청도', '청송', '칠곡', '포항']
Jeonnam = ['전남', '도지사', '강진', '고흥', '곡성', '광양', '구례', '나주', '담양', '목포', '무안', '보성', '순천', '신안', '여수', '영광', '영암', '완도', '장성', '장흥', '진도', '함평', '해남', '화순']
Jeonbuk = ['전북','도지사', '고창', '군산', '김제', '남원', '무주', '부안', '순창', '완주', '익산', '임실', '장수', '전주', '정읍', '진안']
Chungnam = ['충남', '도지사', '계룡', '공주', '금산', '논산', '당진', '보령', '부여', '서산', '서천', '아산', '예산', '천안', '청양', '태안', '홍성']
Chungbuk = ['충북', '도지사', '괴산', '단양', '보은', '영동', '옥천', '음성', '제천', '증평', '진천', '청주', '충주']
Jeju = ['제주', '특별자치도지사']
Kwangju = ['광주', '광역시장']
Daegu = ['대구', '광역시장', '달성']
Daejeon = ['대전','광역시장']
Busan = ['부산','광역시장', '기장']
Seoul = ['서울','특별시장']
Ulsan = ['울산', '광역시장', '울주']
Incheon = ['인천', '광역시장', '강화', '옹진']
Sejong = ['세종', '특별자치시장']

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
        endMonth = int(startTime[0:endMonthIndex])
        endDay = int(startTime[endMonthIndex+1:endDayIndex])
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

def getEE(curMonth, curDay, Location1, Location2):
    try:
        ETL = EmotifyTimeList.objects.get(ETLMonth=curMonth, ETLDay = curDay)
    except ObjectDoesNotExist:
        print(str(curMonth) + " " + str(curDay) + 'No such ETL')
        return False

    try:
        ELL = EmotifyLocationList.objects.get(ELLLocation1 = Location1, ELLLocation2 = Location2)
    except ObjectDoesNotExist:
        print(str(Location1) + " " + str(Location2) + 'No such ELL')
        return False

    try:
        EE = EmotifyElement.objects.get(EEDate = ETL, EELocation = ELL)
    except ObjectDoesNotExist:
        print('No such EE')
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
    while(True):

        EE = getEE(curMonth, curDay, Location1, Location2)
        if EE is not False:
            Happy = Happy + EE.EEHappy
            Sad = Sad + EE.EESad
            Surprise = Surprise + EE.EESurprise
            Anger = Anger + EE.EEAnger
            for type in [1,2,3,4]:
                for DictElem in EmotifyDictionary.objects.filter(EDElement = EE, EDType = type):
                    print('Type = '+str(type))
                    iteration = 0
                    for DictEntry in EmotifyDictEntry.objects.filter(EDEContainer = DictElem).order_by('-EDEValue'):
                        print(DictEntry.EDEValue)
                        if iteration == 20:
                            break
                        try:
                            EmotionDict[(DictElem.EDType)-1][DictEntry.EDEKey] = EmotionDict[(DictElem.EDType)-1][DictEntry.EDEKey] + DictEntry.EDEValue
                        except KeyError:
                            EmotionDict[(DictElem.EDType)-1][DictEntry.EDEKey] = DictEntry.EDEValue
                        iteration = iteration + 1


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

    sortedHappy = sorted(HappyDict.items(), key=operator.itemgetter(1))[0:5]
    sortedSad = sorted(SadDict.items(), key=operator.itemgetter(1))[0:5]
    sortedSurprise = sorted(SurpriseDict.items(), key=operator.itemgetter(1))[0:5]
    sortedAnger = sorted(AngerDict.items(), key=operator.itemgetter(1))[0:5]

    context = {'result':'success'}
    context['Happy'] = Happy
    context['Sad'] = Sad
    context['Surprise'] = Surprise
    context['Anger'] = Anger

    context['HaKeyword'] = sortedHappy
    context['SaKeyword'] = sortedSad
    context['SuKeyword'] = sortedSurprise
    context['AnKeyword'] = sortedAnger

    return context
