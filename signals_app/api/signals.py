from django.dispatch import Signal, receiver 
import time, threading
from django.db.models.signals import pre_save
from .models import Books

signal = Signal()

count = 0

@receiver(signal)
def signal_handler_0(sender, number, **kwargs):
    print("Receiver running on thread  :",threading.current_thread().getName())
    global count
    count += 1
    time.sleep(10)

@receiver(signal)
def signal_handler(sender, number, **kwargs):
    print("Count : ",count)

@receiver(pre_save, sender=Books)
def model_signal(sender , instance , **kwargs):
    instance.name = "updated"



