from django.shortcuts import render
from django.http import HttpResponse
from .signals import signal 

def index(request,number):
    if number == 69:
        signal.send(sender=None, number = number)
    return HttpResponse("Hello world")


