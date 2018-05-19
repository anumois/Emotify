from django.shortcuts import render
import requests
from . import visualLib
from . import serve
from .models import EmotifyTimeList

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

# Create your views here.
def index(request):
    TimeContext = []
    for ETL in EmotifyTimeList.objects.all():
        ETLTuple = str(ETL.ETLMonth) + "월 " + str(ETL.ETLDay) + "일"
        TimeContext.append(ETLTuple)
    context = {'TimeContext' : TimeContext}

    if request.method == 'GET':
        try:
            return display(request,[request.GET['indexLocation'],request.GET['indexLocation2']], request.GET['startTime'], request.GET['endTime'])
        except KeyError:
            return render(request, 'index.html', context)
    return render(request, 'index.html', context)

def display(request, location, startTime, endTime):
    sOut = serve.serverOut(location, startTime, endTime)
    context = visualLib.regContext(location, sOut)
    
    try:
        if context['result'] == 'success':
            return render(request, 'display.html', context)
        else:
            return notFound(request)
    except KeyError:
        return notFound(request)


def notFound(request):
    return render(request,'notFound.html')
