import RPi.GPIO as gpio
from time import sleep

class Robot():
    led=2

    def __init__(self):
        # Modo de operacion de los pines 
        gpio.setmode(gpio.BCM)
        #Configuracion de lso pines 
        gpio.setup(self.led, gpio.OUT)
    def Encender(self):
        gpio.output(self.led,gpio.HIGH)
    def Apagar(self):
        gpio.output(self.led,gpio.LOW)

# Programa principal 
myrobot=Robot()
myrobot.Encender()
sleep(2)
myrobot.Apagar()
sleep(2)
print("fin del programa")
gpio.cleanup()