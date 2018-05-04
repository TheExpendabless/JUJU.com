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


from django.shortcuts import render
# Django自带的用户认证、登录与注销方法
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.db.models import Q
from django.views.generic.base import  View
from . import  models
from .models import UserProfile
from .forms import LoginForm, RegisterForm, UserInfoForm, ResetPwdForm

# pure pagination开源库进行分页
from django.shortcuts import render_to_response

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def home(request):
    if request.method == "GET":
        # 数据库中数据按照时间降序排列，此处取出前四条数据
        newslist = models.newsFlash.objects.all()[:4]
        return render(request, 'home.html',{"newslist":newslist})
def contact(request):
    return render(request, 'contact.html')
def index(request):
    return render(request,'index.html')
def search_community(request,kind):
    return render(request, 'search_community.html',{'kind':kind})
def user_register(request):
    if request.method == "GET":
        return render(request,'register.html')
    elif request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('username','')
            if UserProfile.objects.filter(username=user_name):
                return render(
                    request,"register.html",{
                        "register_form": register_form,"msg": "用户已存在"})
            pass_word = request.POST.get('password',' ')
            repeat_psw = request.POST.get('repeat',' ')
            if pass_word == repeat_psw:
                user_profile = UserProfile()
                user_profile.username = user_name
                # 密码不可明文存储，通过make_password方法加密
                user_profile.password = make_password(pass_word)
                user_profile.save()
                return render(request,'login.html')
            else:
                return render(
                    request,"register.html",{
                        "register_form": register_form,"msg": "两次输入密码不一致"})
        else:
            return render(request,'register.html',{"msg": "用户名或密码不合法"})


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

def user_login(request):
    if request.method == "GET":
        return render(request,'login.html')
    elif request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username','')
            pass_word = request.POST.get('password',' ')
            # 成功返回user对象,失败返回null
            user = authenticate(username=user_name,password=pass_word)
            if user is not None:
                login(request,user)
                return render(request,'home.html')
            else:
                return render(request,'login.html',{"msg": "用户名或密码错误!"})
        else:
            return render(request,'login.html',{"msg": "用户名或密码缺失"})

# 用户退出
def user_logout(request):
    logout(request)
    return render(request,'home.html',{})

def user_settings(request):
    if request.method == "GET":
        return render(request,"settings.html",{})

def user_info(request):
    if request.method == "POST":
        # return render(request,'settings.html',{ })
        # 不像用户咨询是一个新的。需要指明instance 不然会变成新增用户
        user_info_form = UserInfoForm(request.POST,instance=request.user)
        # return render(request,'settings.html')
        if user_info_form.is_valid():
            user_info_form.email = request.POST.get("email",'')
            user_info_form.mobile = request.POST.get("mobile",'')
            user_info_form.save()
            return render(request,'settings.html',{})

def reset_pwd(request):
    if request.method == "POST":
        reset_form = ResetPwdForm(request.POST)
        # return render(request,'settings.html')
        user = request.user
        if reset_form.is_valid():
            oldpwd = request.POST.get("oldpassword")
            newpwd = request.POST.get("newpassword","")
            repwd = request.POST.get("repeatpassword","")
            if user.check_password(oldpwd):
                # 如果两次密码不相等，返回错误信息
                if newpwd != repwd:
                    return render(request,'settings.html',{"msg": "两次输入密码不一致"})
                user.password = make_password(repwd)
                user.save()
                logout(request)
                return render(request,'login.html',{})
            else:
                return render(request,'settings.html',{"msg": "原始密码不符，请重新输入"})
        # 验证失败说明密码位数不够。
        else:
            return render(request,"settings.html",{
                "modiypwd_form": reset_form,"msg": "密码输入格式有误"})


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

# 从数据库获取新闻资讯返回
def news(request):

    newslist = models.newsFlash.objects.all().order_by('id')

    # 对新闻进行分页
    try:
        page = request.GET.get('page',1)
    except PageNotAnInteger:
        page = 1
    p = Paginator(newslist,6,request=request)

    news = p.page(page)
    return render(request, 'news.html',{"newslist":news})