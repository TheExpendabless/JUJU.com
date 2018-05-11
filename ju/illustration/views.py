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
from django.contrib import messages
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
from .models import UserProfile,UserCollect
from .forms import LoginForm, RegisterForm, UserInfoForm, ResetPwdForm,UserCollectForm

# pure pagination开源库进行分页
from django.shortcuts import render_to_response

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def home(request):
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
                newslist = models.newsFlash.objects.all()[:4]
                return render(request,'home.html',{"newslist": newslist})
            else:
                return render(request,'login.html',{"msg": "用户名或密码错误!"})
        else:
            return render(request,'login.html',{"msg": "用户名或密码缺失"})

# 用户退出
def user_logout(request):
    logout(request)
    newslist = models.newsFlash.objects.all()[:4]
    return render(request,'home.html',{"newslist": newslist})

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
    community=models.Community.objects.filter(title=community_title)
    if len(community)==0:
        messages.warning(request,'抱歉，查找失败')
        return render(request,'index.html')
    community = community[0]
    collect_status = 0
    if request.user.is_authenticated:
        id = community.id
        is_collect = models.UserCollect.objects.filter(user=request.user.username,community_id=int(id))
        if len(is_collect) == 0:
            collect_status = 0
        else:
            collect_status = 1
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
    return render(request,'community_detail.html',{'community':community,'lng':lng,'lat':lat,'count':count,'collect_status':collect_status})

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

def collect(request):
     if request.method == "POST":
         # 默认值为0 防止程序崩盘
         id = request.POST.get('community_id',0)

         # 收藏与已收藏取消收藏
         # 判断用户是否登录:即使没登录会有一个匿名的user
         if not request.user.is_authenticated:
             # 未登录时返回json提示未登录，跳转到登录页面在ajax中实现
             # return HttpResponse('{"status":0, "msg":"用户未登录"}',content_type='application/json')
             data = json.dumps({"status":0, "msg": "用户未登录"},cls=DjangoJSONEncoder)
             return HttpResponse(data)
         exist_records = UserCollect.objects.filter(user=request.user.username,community_id=int(id))
         if exist_records:
             # 如果记录已经存在， 则表示用户取消收藏
             exist_records.delete()
             # return HttpResponse('{"status":1, "msg":"收藏"}',content_type='application/json')
             data = json.dumps({"status": 1,"msg": "关注小区"},cls=DjangoJSONEncoder)
             return HttpResponse(data)
         else:
             user_fav = models.UserCollect()
             # 默认值为0 剔除默认
             if int(id) > 0:
                 user_fav.community_id = int(id)
                 user_fav.user = request.user.username
                 user_fav.save()
                 # return HttpResponse('{"status":1, "msg":"已关注"}',content_type='application/json')
                 data = json.dumps({"status": 1,"msg": "已关注"},cls=DjangoJSONEncoder)
                 return HttpResponse(data)
             else:
                 # return HttpResponse('{"status":0, "msg":"收藏出错"}',content_type='application/json')
                 data = json.dumps({"status": 0,"msg": "收藏出错"},cls=DjangoJSONEncoder)
                 return HttpResponse(data)

def show_collect(request):
    if request.method == "GET":
        user = request.user.username
        fav_id_list = UserCollect.objects.filter(user=user)
        user_fav_list = []
        for fav_comminuty in fav_id_list:
            id = fav_comminuty.community_id
            user_fav_list.append(models.Community.objects.get(id=id))
        # return render(request,'collect.html',{
        #     "user_fav_list": user_fav_list,
        # })

        try:
            page = request.GET.get('page',1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(user_fav_list,10,request=request)

        news = p.page(page)
        return render(request,'collect.html',{"user_fav_list": user_fav_list, "user_fav_list_page": news})

def invest_ass(request):
    return render(request,'invest_ass.html',{})

def price_predict(request):
    if request.method == "GET":
        return render(request,'price_predict.html',{})
    if request.method == "POST":
        # 可以设置默认值但是没设置
        community = request.POST.get('community')

        exist_records = models.Community.objects.filter(title=community)
        if not exist_records:
            data = json.dumps({"status": 0,"msg": "不存在该小区"},cls=DjangoJSONEncoder)
            return HttpResponse(data)
        else:
            find_com = exist_records[0]
            if len(find_com.taglist) == 0:
                near_sub = 0
            else:
                near_sub = 1
            if find_com.cost == "暂无信息":
                wuye_price = 0.75
            else:
                wuye_price = find_com.cost
                length = len(wuye_price)
                wuye_price = wuye_price[0:length-6]
                if not wuye_price.isdigit():
                    wuye_price = wuye_price[0:3]
            if find_com.price == "暂无":
                com_price = 50251
            else:
                com_price = find_com.price
            data = json.dumps({"status": 1,"msg": "查询到小区信息","near_sub":near_sub,"wuye_price":wuye_price,"com_price":com_price},cls=DjangoJSONEncoder)
            return HttpResponse(data)

def buy_or_rent(request):
    return render(request,'buy_or_rent.html')
