from django.urls import path
from django.conf.urls import url
from . import views 
from django.conf import settings
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns =[
    
    path('',views.home,name="home"),
    path('index/',views.index,name="index"),
    path('contact/',views.contact,name="contact"),
    path('ABOUT/',views.ABOUT,name="ABOUT"),
    path('login/',views.loginPage,name="login"),
    path('register/',views.registerPage,name="register"),
    path('logout/',views.logoutUser,name="logout"),
    url(r'^$',views.button),
    url(r'^output',views.output,name="output"),
    url(r'^external',views.external),
]