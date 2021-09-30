from tkinter import Button, Tk
from time import sleep
from tkinter.constants import X
import RPi.GPIO as gpio

#definir el modo 
gpio.setmode(gpio.BCM)
# configuracion del pin 
gpio.setup(2,gpio.OUT)

# Función LED
def encender():
    gpio.output(2,gpio.HIGH)
def apagar():
    gpio.output(2,gpio.LOW)

# Creación de la ventana 
ventana= Tk()
ventana.geometry("400x200")
ventana.title("Encender Led")
# Creación de un boton 
bt1=Button(ventana, text="Encneder LED",command=encender)
bt1.place(x=30, y=40)

bt2=Button(ventana, text="Apagar LED", command=apagar)
bt2.place(x=200,y=40)

ventana.mainloop()

# Limpiar lierar pines 
gpio.cleanup()
