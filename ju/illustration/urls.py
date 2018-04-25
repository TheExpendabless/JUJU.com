from django.contrib import admin
from django.urls import path,include
from illustration import views
app_name='illustration'
urlpatterns = [
    path('index/', views.index,name='index'),
    path('detail/', views.detail, name='detail'),
    path('register/', views.register,name='register'),
    path('login/', views.login,name='login'),
]
