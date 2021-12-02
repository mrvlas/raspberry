
# Python Script
# https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/

import RPi.GPIO as GPIO          
from time import sleep

# MOTOR 1
in1 = 24
in2 = 23
ena = 25
# MOTOR 2
in3=17
in4=27
enb=22


# Modo de configuración de los pines
GPIO.setmode(GPIO.BCM)
# Configuración de variables como salida
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(ena,GPIO.OUT)

GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)


# Por defecto dejamos todo los pines GPIO apagados
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)


p1=GPIO.PWM(ena,1000)
p1.start(100)
p2=GPIO.PWM(enb,1000)
p2.start(100)


print("avanzar")
GPIO.output(in1,GPIO.HIGH)
GPIO.output(in3,GPIO.HIGH)
sleep(3)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)

"""
print("Girar")
GPIO.output(in1,GPIO.HIGH)
GPIO.output(in4,GPIO.HIGH)
sleep(3)
"""
sleep(0.5)
print("Retroceder")
GPIO.output(in2,GPIO.HIGH)
GPIO.output(in4,GPIO.HIGH)
sleep(2)

print("Fin del movimiento")
GPIO.output(in2,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

GPIO.cleanup()