from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="index"),
    path("home",views.home,name="home"),
    path("contact",views.contactus,name="contact"),
    path("login",views.login,name="login"),
]