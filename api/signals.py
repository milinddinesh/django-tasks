from django.dispatch import Signal, receiver 
signal = Signal()

@receiver(signal)
def signal_handler_0(sender, number, **kwargs):
    print(number +1 )

@receiver(signal)
def signal_handler(sender, number, **kwargs):
    print("hello world ")


