import RPi.GPIO as gpio
from time import sleep, time

# Declaración de variables
trigger=2 # Salida
echo=20 # Entrada 

# Configuración 
gpio.setmode(gpio.BCM)
gpio.setup(trigger, gpio.OUT)
gpio.setup(echo, gpio.IN)
gpio.output(trigger, gpio.LOW)

try:
    while True:
        print("Entramos al While")
        gpio.output(trigger, gpio.HIGH)
        sleep(0.00001)
        gpio.output(trigger, gpio.LOW)
        t1=time()
        while gpio.input(echo)== gpio.LOW:
            t1=time()
        while gpio.input(echo)== gpio.HIGH:
            t2=time()
        
        t=t2-t1
        d=17000*t
        print("La Distancia es:",round(d,1),"cms")
        sleep(0.2)
except:
    gpio.cleanup()
    print("Saliendo del programa")

