from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('create-room/', views.createroom , name ="create-room" )
]
