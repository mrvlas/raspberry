import RPi.GPIO as gpio
from time import sleep

pulsador=2
led=17
gpio.setmode(gpio.BCM)
gpio.setup(pulsador, gpio.IN)
gpio.setup(led, gpio.OUT)

gpio.output(led, gpio.LOW)

while True:
    if gpio.input(pulsador)==gpio.HIGH:
        print("Pulsado")
        gpio.output(led, gpio.LOW)
    else:
        gpio.output(led, gpio.HIGH)

    
