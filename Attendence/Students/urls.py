from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="user_home"),
    path('read_all_users', views.getusersCust, name="user_home"),

    # at one
    path("one/<str:pk>", views.getusersCust_one, name="home_one"),


    path("create", views.createusersCust, name="create"),

    path("update/<str:pk>/", views.update_oneuser, name="update"),

    path("delete/<str:pk>/", views.usercustdelete, name="delete"),

    # attendence
    path('attendence_all', views.allAttendence, name="attendence_all"),
    path('getAttendenceof/<str:pk>/',
         views.getAttendenceof, name="attendence_of_user"),

    path('fill_attendence', views.fillattendence, name="fill_attendence"),
]
