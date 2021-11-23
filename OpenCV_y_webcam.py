"""
	Tomar foto con Python y opencv

	@date 20-03-2018
	@author parzibyte
	@see https://www.parzibyte.me/blog
"""

import cv2


"""
	En este caso, 0 quiere decir que queremos acceder
	a la cámara 0. Si hay más cámaras, puedes ir probando
	con 1, 2, 3...
"""
cap = cv2.VideoCapture(1)

leido, frame = cap.read()
print(leido)

if leido == True:
	cv2.imwrite("foto.png", frame)
	print("Foto tomada correctamente")
else:
	print("Error al acceder a la cámara")

"""
	Finalmente liberamos o soltamos la cámara
"""
cap.release()