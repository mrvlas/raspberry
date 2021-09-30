from time import sleep 
import RPi.GPIO as gpio 
# definir el modo 
gpio.setmode(gpio.BCM)
# Configuracion del componente 
gpio.setup(2, gpio.OUT)
contador=0
while contador<10:
	gpio.output(2,gpio.HIGH)
	print("encendido")
	sleep(2)
	gpio.output(2,gpio.LOW) 
	sleep(1)
	contador+=1
# Se limpian los pines gpio    
gpio.cleanup()
