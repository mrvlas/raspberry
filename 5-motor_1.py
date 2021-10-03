
import RPi.GPIO as GPIO          
from time import sleep

in1 = 24
in2 = 23

GPIO.setmode(GPIO.BCM)

GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)

print("inicio del movimiento")
GPIO.output(in1,GPIO.HIGH)
GPIO.output(in2,GPIO.LOW)
sleep(10)

print("Fin del movimiento")
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)

GPIO.cleanup()