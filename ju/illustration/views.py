from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . import  models
from django.db.models import Avg,Count
from django.shortcuts import render,redirect
from django.conf import settings
import json
from django.forms.models import model_to_dict
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
from django.contrib import auth
from django.core.serializers import serialize
from django.core.serializers.json import  DjangoJSONEncoder
from django.contrib.auth.hashers import make_password
from django.db.models import F
import requests
import datetime

# Create your views here.
def home(request):
    return render(request, 'home.html')
def contact(request):
    return render(request, 'contact.html')
def index(request):
    return render(request,'index.html')
def search_community(request,kind):
    return render(request, 'search_community.html',{'kind':kind})
def register(request):
    return render(request,'register.html')
# 用户登录
def bizcircle_community(request):
    input = request.POST.get('input')
    data = models.Community.objects.filter(bizcircle=input).values()
    data = json.dumps(list(data), cls=DjangoJSONEncoder, ensure_ascii=False)
    return HttpResponse(data)

def station_community(request):
    station = request.POST.get('station')
    data = models.Community.objects.filter(taglist__contains=station).values()
    data = json.dumps(list(data), cls=DjangoJSONEncoder, ensure_ascii=False)
    return HttpResponse(data)

def login(request):
    return render(request,'login.html')

# 用户退出
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/blog')


def community_detail(request):
    community_title=request.POST.get('community')
    community=models.Community.objects.get(title=community_title)
    address="上海市"+community.district+community_title
    parameters1 = {'address': address, 'key': 'f14f3c4d3e03c58b2cb53fdacb49ecb7'}
    base1 = 'http://restapi.amap.com/v3/geocode/geo'
    response = requests.get(base1, parameters1)
    answer = response.json()
    lng=answer['geocodes'][0]['location'].split(',')[0]
    lat=answer['geocodes'][0]['location'].split(',')[1]
    base2='http://restapi.amap.com/v3/place/around'
    parameters2={'location':answer['geocodes'][0]['location'], 'keywords':'医院','type':'090000','radius':1000,'key': 'f14f3c4d3e03c58b2cb53fdacb49ecb7'}
    count = requests.get(base2, parameters2).json()['count']
    return render(request,'community_detail.html',{'community':community,'lng':lng,'lat':lat,'count':count})

def his_price(request):
    unitprice_infos=[]
    dateList=['2017-01', '2017-02', '2017-03', '2017-04', '2017-05', '2017-06', '2017-07', '2017-08', '2017-09','2017-10', '2017-11', '2017-12',
              '2018-01', '2018-02', '2018-03']
    for date in dateList:
        unitprice_infos.append(models.Sellinfo.objects.filter(dealdate__contains=date).exclude(unitprice='下载APP查看成交>').aggregate(avgprice=Avg('unitprice')))
    return render(request,'his_price.html',{'unitprice_infos':unitprice_infos})
def his_detail(request):
    return render(request,'his_detail.html')
def community_info(request):
    return render(request,'community_info.html')
def community_hisprice(request):
    community=request.POST.get('community')
    data=models.Sellinfo.objects.filter(community=community).exclude(unitprice='下载APP查看成交>').values('dealdate','unitprice').order_by('dealdate')
    data = json.dumps(list(data), cls=DjangoJSONEncoder)
    return HttpResponse(data)

def community_hisdetail(request):
    community = request.POST.get('community')
    data=models.Houseinfo.objects.filter(community=community).values('housetype').annotate(Count('housetype'))
    data = json.dumps(list(data), cls=DjangoJSONEncoder,ensure_ascii=False)
    return HttpResponse(data)
def district_hisprice(request):
    district = request.POST.get('district')
    data = models.Sellinfo.objects.filter(district=district).exclude(unitprice='下载APP查看成交>').values('dealdate','unitprice').order_by('dealdate')
    data = json.dumps(list(data), cls=DjangoJSONEncoder, ensure_ascii=False)
    return HttpResponse(data)
