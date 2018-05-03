from django.contrib import admin
from django.urls import path,include
from illustration import views
app_name='illustration'
urlpatterns = [
    path('home/',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('index/', views.index,name='index'),
    path('community_detail/', views.community_detail, name='community_detail'),
    path('register/', views.register,name='register'),
    path('login/', views.login,name='login'),
    path('userinfo/', views.login,name='userinfo'),
    path('settings/', views.login,name='settings'),
    path('logout/', views.login,name='logout'),
    path('bizcircle_community/',views.bizcircle_community),
    path('station_community/',views.station_community),
    path('search_community/<str:kind>', views.search_community,name='search_community'),
    path('his_price/',views.his_price,name='his_price'),
    path('his_detail/',views.his_detail,name='his_detail'),
    path('community_info/',views.community_info),
    path('community_hisprice/',views.community_hisprice,name='community_hisprice'),
    path('community_hisdetail/',views.community_hisdetail,name='community_hisdetail'),
    path('district_hisprice/',views.district_hisprice,name='district_hisprice'),
]
