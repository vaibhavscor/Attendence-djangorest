from django.shortcuts import render, redirect
from .models import Users_custom, Attendence
from .serializers import User_customSerializer, Attendence_user_serializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def home(request):
    api_urls = {
        'one/<str:pk>': "to see specific user using User id",
        'create': "to create a new user",
        'update/<str:pk>/': "to update specific user data ",
        'delete/<str:pk>/': "to delete a user",
        'read_all_users': "to read all users",
        'attendence_all': "to see all the attendence",
        'getAttendenceof/<str:pk>/': "to get the attendence of specific user",
        'fill_attendence': "to Fill the attendence",
    }
    return Response(api_urls)


@api_view(['GET'])
def getusersCust(request):
    USR = Users_custom.objects.all()
    serilizer = User_customSerializer(USR, many=True)
    return Response(serilizer.data)


@api_view(['GET'])
def getusersCust_one(request, pk):
    tasks = Users_custom.objects.get(id=pk)
    # many - do you want to serlize many objects or one
    serilizer = User_customSerializer(tasks, many=False)
    return Response(serilizer.data)


@api_view(['POST'])
def createusersCust(request):
    serilizer = User_customSerializer(data=request.data)
    if serilizer.is_valid():
        serilizer.save()
    return Response(serilizer.data)


@api_view(['POST'])
def update_oneuser(request, pk):
    task = Users_custom.objects.get(id=pk)
    serilizer = User_customSerializer(instance=task, data=request.data)

    if serilizer.is_valid():
        serilizer.save()

    return Response(serilizer.data)


@api_view(['DELETE'])
def usercustdelete(request, pk):
    userc = Users_custom.objects.get(id=pk)
    userc.delete()
    return Response('ITEM DELETED')


# Attendence


@api_view(['GET'])
def allAttendence(request):
    user_attend = Attendence.objects.all()
    serilizer = Attendence_user_serializer(user_attend, many=True)
    # print(serilizer.data)
    return Response(serilizer.data)


@api_view(['GET'])
def getAttendenceof(request, pk):
    tasks = Attendence.objects.filter(user=pk)
    # many - do you want to serlize many objects or one
    serilizer = Attendence_user_serializer(tasks, many=True)
    return Response(serilizer.data)


@api_view(['POST'])
def fillattendence(request):
    serilizer = Attendence_user_serializer(data=request.data)
    if serilizer.is_valid():
        serilizer.save()
    return Response(serilizer.data)
