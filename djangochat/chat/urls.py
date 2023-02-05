from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:room>/', views.room, name='room'), # pass dynamic room str to room()
    path('checkview', views.checkview, name= 'checkview'), # checks if the room entered in home exists
    path('send', views.send, name= 'send'), #after user submits message in chatroom
    path('getMessages/<str:room>/', views.getMessages, name = 'getMessages'),

]