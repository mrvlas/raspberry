from tkinter import Button, Message, Tk, messagebox 
ventana=Tk()

def msn():
    print("Aceptar")



ventana.geometry("400x400")
bt1=Button(ventana,text="Aceptar", command=msn)
bt1.place(x=30, y=30)

ventana.mainloop()
