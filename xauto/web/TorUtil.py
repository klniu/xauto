from stem import Signal
from stem.control import Controller

def changeIP(password):
    with Controller.from_port(port = 9051) as controller:
      controller.authenticate(password)
      controller.signal(Signal.NEWNYM)
