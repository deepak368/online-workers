"""onlineworkers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.shortcuts import render
from .views import UserRegisterView,UserLoginView,User_logout,FeedbackView,\
    feedbacklist,UserRequestView,List_userRequest,List_request,requestEditView,\
    requestDeleteView,WorkerRequestView,list_workerrequest,Notification,search_view,workerreqRemove,BookView,Bookdetails


urlpatterns = [
    path("",UserLoginView.as_view(),name="login"),
    path("register",UserRegisterView.as_view(),name="register"),
    path("logout",User_logout,name="logout"),
    path("feedback",FeedbackView.as_view(),name="feedback"),
    path("feedback-list",feedbacklist.as_view(),name="feedback-list"),
    path("error",lambda request:render(request,"work/error.html"),name="error"),
    path("user-request",UserRequestView.as_view(),name="user-req"),
    path("userreq-replay",lambda request:render(request,"work/userrequestrply.html"),name="userreq-rply"),
    path("user-page",lambda request:render(request,"work/index.html"),name="userpg"),
    path("requests-list",List_userRequest.as_view(),name="req-list"),
    path("worker-request/<int:pk>",WorkerRequestView.as_view(),name="worker-request"),
    path("worker-reply",lambda request:render(request,"work/WRreply.html"),name="worker-reply"),
    path("workerrequest-list",list_workerrequest.as_view(),name="workreq-list"),
    path("wages",lambda request:render(request,"work/wages.html"),name="wages"),
    path("indivituallist",List_request.as_view(),name="list"),
    path("request-edit/<int:pk>",requestEditView.as_view(),name="request-edit"),
    path("request-delete/<int:pk>",requestDeleteView.as_view(),name="request-delete"),
    path("notification",Notification.as_view(),name="notification"),
    path("search",search_view,name="search"),
    path("workerrequest-delete/<int:pk>",workerreqRemove.as_view(),name="workerrequest-delete"),
    path("book/<int:pk>",BookView.as_view(),name="book"),
    path("booked-details",Bookdetails.as_view(),name="booked"),
    path("final-reply",lambda request:render(request,"work/finalreply.html"),name="final")


]
