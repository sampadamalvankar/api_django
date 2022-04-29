from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from API.models import User,Client,Project
from API.serializers import UserSerializer,ClientSerializer,ProjectSerializer


# Create your views here.

@csrf_exempt
def userapi(request,id=0):
    if request.method=='GET':
        user = User.objects.all()
        user_serializer=UserSerializer(user,many=True)
        return JsonResponse(user_serializer.data,safe=False)
    elif request.method=='POST':
        user_data=JSONParser().parse(request)
        user_serializer=UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Added Successfully")
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        user_data=JSONParser().parse(request)
        user=User.objects.get(UserID=user_data['UserID'])
        user_serializer=UserSerializer(user,data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("update Successfully",safe=False)
        return JsonResponse("Failed To update")
    elif request.method=='DELETE':
        user=User.objects.get(UserId=id)
        user.delete()
        return JsonResponse("Deleted Successfully",safe=False)


@csrf_exempt
def clientapi(request,id=0):
    if request.method=='GET':
        client = Client.objects.all()
        client_serializer=ClientSerializer(client,many=True)
        return JsonResponse(client_serializer.data,safe=False)
    elif request.method=='POST':
        client_data=JSONParser().parse(request)
        client_serializer=ClientSerializer(data=client_data)
        if client_serializer.is_valid():
            client_serializer.save()
            return JsonResponse("Added Successfully")
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        client_data=JSONParser().parse(request)
        client=Client.objects.get(ClientName=client_data['ClientName'])
        client_serializer=ClientSerializer(client,data=client_data)
        if client_serializer.is_valid():
            client_serializer.save()
            return JsonResponse("updated Successfully",safe=False)
        return JsonResponse("Failed To update")
    elif request.method=='DELETE':
        client=Client.objects.get(ClientId=id)
        client.delete()
        return JsonResponse("Status code",safe=False)#204


@csrf_exempt
def projectapi(request,id=0):
    if request.method=='GET':
        project = Project.objects.all()
        project_serializer=ProjectSerializer(project,many=True)
        return JsonResponse(project_serializer.data,safe=False)
    elif request.method=='POST':
        project_data=JSONParser().parse(request)
        project_serializer=ProjectSerializer(data=project_data)
        if project_serializer.is_valid():
            project_serializer.save()
            return JsonResponse("Added Successfully")
        return JsonResponse("Failed to Add",safe=False)
