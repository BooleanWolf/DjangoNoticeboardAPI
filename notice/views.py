from django.shortcuts import render
from django.http import HttpResponse

from django.http import JsonResponse
from rest_framework.decorators import api_view 
from rest_framework.response import Response

# Create your views here.

def say_hello(request):
    
    return HttpResponse("Hello World")


def say_bye(request):
    return HttpResponse("Coooooool")


@api_view(['GET'])
def customViewApi(request):
    Person = { 'Person1': {'Name': 'Sourav', 'Age' : 90, 'Univeristy': "AIUB", }, 'Person2': {'Name': 'Tamim', 'Age' : 90, 'Univeristy': "AIUB", }}



    return Response(Person)