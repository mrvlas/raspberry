from time import sleep
# Se importa la libreria 
import RPi.GPIO as GPIO
# Se establece el modo de los pines 
GPIO.setmode(GPIO.BCM)
#Configuración del pin a programar
GPIO.setup(2, GPIO.OUT)
# APAGAMOS EL LED
GPIO.output(2,GPIO.LOW)
print("apagado")
sleep(5)
GPIO.output(2, GPIO.HIGH)
print("Encendido")
sleep(2)
GPIO.output(2, GPIO.LOW)
print("apagado")

