from django.shortcuts import render
from django.http import HttpResponse
from . import  models
# Create your views here.
def index(request):
    return render(request,'index.html')
def register(request):
    return render(request,'register.html')
def login(request):
    return render(request,'login.html')
def detail(request):
    community_title=request.POST.get('community')
    community=models.Community.objects.get(title=community_title)
    return render(request,'detail.html',community)