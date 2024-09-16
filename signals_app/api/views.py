from django.shortcuts import render
from django.http import HttpResponse
from .signals import signal 
from .models import Books
from django.db import transaction 

import threading

def index(request,number):
    if number == 69:
        print("View running on thread" ,threading.current_thread().getName())
        signal.send(sender=None, number = number)

    return HttpResponse("Hello world")

def db_update(request):
    with transaction.atomic():
        Books.objects.create(name="book1")
    print(Books.objects.all().values())

    return HttpResponse("Hello world")
