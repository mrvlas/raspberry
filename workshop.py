from Tkinter import *
import time
import picamera
import RPi.GPIO as GPIO  
import numpy as np
import io
from datetime import datetime, timedelta

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)   
GPIO.setup(17, GPIO.IN, GPIO.PUD_UP)  

camera = picamera.PiCamera()
ON = True

zoom = 1.0
previewTime = 3
awbcount = 0
effectno = 0
delay = 5
threshPercent = 1.8
step = 1
numImages = 1
captureCount = 0
numSav = 0

def centre_window(w, h):
	ws = root.winfo_screenwidth()
	hs = root.winfo_screenheight()
	x = (ws/2) + 400
	y = (hs/2) - 285 
	root.geometry('%dx%d+%d+%d' % (w, h, x, y))

def brightUp():
        if camera.brightness < 100:
                camera.brightness += 5
        else:
                camera.brightness = 100
	w.set(camera.brightness)
#	print "Brightness", camera.brightness
	preview()

def brightDown():
	if camera.brightness < 10:
		camera.brightness = 5
	else:
		camera.brightness -= 5
#        print "Brightness", camera.brightness
	w.set(camera.brightness)
	preview()
	
def rotate():
	camera.rotation += 90
	print "Rotation", camera.rotation, "degrees"
	preview()

def hflip():
	if camera.hflip == True:
                camera.hflip = False
	else:
		camera.hflip = True
	print "hFlip", camera.hflip
	preview()

def vflip():
	if camera.vflip == True:
		camera.vflip = False
	else:
		camera.vflip = True
        print "vFlip", camera.vflip
	preview()

def prevTime():
	global previewTime
	previewTime += 1
        print "Preview time", previewTime, "s"
	return previewTime
	preview()

def preview():
	camera.preview_fullscreen = False
	camera.preview_window = (170, -120, 860, 950)
	camera.video_stabilization = True
	camera.brightness=w.get()
	camera.start_preview()
	print "Brightness",camera.brightness
        camera.contrast=y.get() 
        print "Contrast",camera.contrast
        camera.saturation=xy.get()
        print "Saturation",camera.saturation
	for t in range (previewTime, 0, -1):
		camera.brightness = w.get()
       		time.sleep(1)
	
def still():
        print "Press the Button!"
        camera.preview_fullscreen = False
        camera.preview_window = (150, 50, 860, 540)
        camera.start_preview()
        GPIO.wait_for_edge(17, GPIO.FALLING) 
	time.sleep(1)
	print "Brightness",camera.brightness
        print "Contrast",camera.contrast
        camera.capture('/home/pi/Desktop/images/image.jpg')
	camera.stop_preview()

def vid():
        print "Press the Button!"
        camera.preview_fullscreen = False
        camera.preview_window = (150, 50, 860, 540)
        camera.start_preview()
        GPIO.wait_for_edge(17, GPIO.FALLING)
        camera.start_recording('/home/pi/Desktop/images/video.h264')
        time.sleep(1)
	GPIO.wait_for_edge(17, GPIO.FALLING)
	camera.stop_recording()
        camera.stop_preview()

def sat():
        camera.saturation=xy.get()
	if camera.saturation < -99:
		camera.saturation += 5
	elif camera.saturation > 99:
		camera.saturation -= 5
	else:
		camera.saturation +=5
	xy.set(camera.saturation)
	preview()

def sharp():
        camera.sharpness += 10
        print "Sharpness", camera.sharpness
        preview()

def zoomIn():
        global zoom
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
	if zoom >= 0.7:
		zoom -= 0.05
		x = (ws/2) - 0.5 * 400/(1 - zoom)
		y = (hs/2) - 0.5 * 285/(1 - zoom)
        	camera.zoom = (x, y, zoom, zoom)
	       	print "Zoom", zoom, "%"
	else:
		print "Max zoom!"
		zoom = 0.7
		print "Zoom", zoom, "%"
        preview()

def zoomOut():
        global zoom
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        if zoom <= 1.3:
                zoom += 0.05
                x = (ws/2) - 0.5 * 400/(1 - zoom)
                y = (hs/2) - 0.5 * 285/(1 - zoom)
                camera.zoom = (x, y, zoom, zoom)
                print "Zoom", zoom, "%"
        else:
                print "Min zoom!"
                zoom = 1.3
                print "Zoom", zoom, "%"
        preview()

def contrast():
	camera.contrast = y.get()
        if camera.contrast < -99:
                camera.contrast += 5
        elif camera.contrast > 99:
                camera.contrast -= 5
        else:
		camera.contrast += 5
        print "Contrast", camera.contrast
        y.set(camera.contrast)
	preview()

def led():      
	global ON
	if ON == True:
		camera.led = False
                ON =  False
        else:
                ON = True
		camera.led = True
        print "LED on", ON

def fav():
        global previewTime
        previewTime = 3
	print "Preview time",previewTime
       	camera.brightness = w.get()
        print "Brightness",camera.brightness
       	camera.rotation = 0
	print "Rotation",camera.rotation
	camera.hflip = False
	print "hFlip",camera.hflip
	camera.vflip = False
	print "vFlip",camera.vflip
	camera.saturation = 0
	print "Saturation",camera.saturation
	camera.sharpness = 0
	print "Sharpness",camera.sharpness
	camera.contrast = y.get()
	print "Contrast",camera.contrast
	camera.AWB_MODES['auto']
	print "AWB auto"
	camera.image_effect = 'none'
	print "Image effect",camera.image_effect
	preview()

def awb():
	global awbcount
        awbcount += 1
	if awbcount == 1:
                camera.AWB_MODES['auto']
		print "AWB auto"
        elif awbcount == 2:
                camera.AWB_MODES['sunlight']
                print "Sunlight"
        elif awbcount == 3:
                camera.AWB_MODES['cloudy']
                print "Cloudy"
        elif awbcount == 4:
                camera.AWB_MODES['shade']
                print "Shade"
        elif awbcount == 5:
                camera.AWB_MODES['tungsten']
                print "Tungsten"
        elif awbcount == 6:
                camera.AWB_MODES['fluorescent']
                print "Fluorescent"
        elif awbcount == 7:
                camera.AWB_MODES['incandescent']
                print "Incandescent"
        elif awbcount == 8:
                camera.AWB_MODES['flash']
                print "Flash"
        elif awbcount == 9:
                camera.AWB_MODES['horizon']
		print "Horizon"
        elif awbcount == 10:
                camera.AWB_MODES['off']
                print "Off"
	else:
		awbcount = 0
	preview()

def effects():
	global effectno
	effectno += 1
	if effectno == 1:
		camera.image_effect = 'none'
	elif effectno == 2:
		camera.image_effect = 'negative'
        elif effectno == 3:
                camera.image_effect = 'solarize'
        elif effectno == 4:
                camera.image_effect = 'sketch'
        elif effectno == 5:
                camera.image_effect = 'denoise'
        elif effectno == 6:
                camera.image_effect = 'emboss'
        elif effectno == 7:
                camera.image_effect = 'oilpaint'
        elif effectno == 8:
                camera.image_effect = 'hatch'
        elif effectno == 9:
                camera.image_effect = 'gpen'
        elif effectno == 10:
                camera.image_effect = 'pastel'
        elif effectno == 11:
                camera.image_effect = 'watercolor'
        elif effectno == 12:
                camera.image_effect = 'film'
        elif effectno == 13:
                camera.image_effect = 'blur'
        elif effectno == 14:
                camera.image_effect = 'saturation'
        elif effectno == 15:
                camera.image_effect = 'colorswap'
        elif effectno == 16:
                camera.image_effect = 'washedout'
        elif effectno == 17:
                camera.image_effect = 'posterise'
        elif effectno == 18:
                camera.image_effect = 'colorpoint'
        elif effectno == 19:
                camera.image_effect = 'colorbalance'
        elif effectno == 20:
                camera.image_effect = 'cartoon'
        elif effectno == 21:
                camera.image_effect = 'deinterlace1'
	elif effectno == 22:
                camera.image_effect = 'deinterlace2'
	print "image effect",camera.image_effect
        preview()

def demo():
        for x in range(1, 10):
		awb()
		preview()
		time.sleep(3)

def wait():
	# Calculate the delay to the start of the next hour
	global delay
#	next_hour = (datetime.now() + timedelta(hours=1)).replace(minute=0, second=0, microsecond=0)
	delay =	yy.get()
#	delay = (next_hour - datetime.now()).seconds
	time.sleep(delay)

def lapse():
	preview()
	wait()
	try:
		while True:
			for filename in camera.capture_continuous('/home/pi/Desktop/images/{timestamp:%d-%m-%H:%M:%S}.jpg'):
				print('%s' % filename[24:])
				wait()
	except KeyboardInterrupt:
		print " CTRL-C detected"
		GPIO.cleanup()
		exit()

def filenames():
	frame = 0
	fileName = time.strftime("/home/pi/Desktop/images/%d-%m-%Y:%H:%M:%S",time.localtime())
	while frame < 1:
		yield '%s%00d.jpg' % (fileName, frame)
		frame += 1

def motion():
	global numImages
	global step
	global captureCount
	global numSav
	global threshPercent
	widthH = 2592
	heightH = 1944
	width = 1440
	height = 1080
	threshold = 30
	threshPercent = zz.get()
	minPixelsChanged = width * height * threshPercent/100	# increase the percentage for less motion sensitivity

	print "Minimum no of Pixels to be Changed=",int(minPixelsChanged)," ie: ",minPixelsChanged/(width*height)*100 ,"%"
	print "Creating in-memory stream"
	stream = io.BytesIO()

	time.sleep(1)
	try:
		while threshold > 0:
			camera.resolution = (1440, 1080)
			print "Cap:", numImages,
			if step == 1:
				stream.seek(0)
				camera.capture(stream, 'rgba',True)
				data1 = np.fromstring(stream.getvalue(), dtype=np.uint8)
				step = 2
			else:
				stream.seek(0)
				camera.capture(stream, 'rgba',True)
				data2 = np.fromstring(stream.getvalue(), dtype=np.uint8)
				step = 1
			numImages = numImages + 1

			if numImages > 4:
				if captureCount <= 0:
					data3 = np.abs(data1 - data2)
					numTriggers = np.count_nonzero(data3 > threshold) / 4 / threshold
					motionThreshold = int(numTriggers*100/minPixelsChanged)
					print "Trig:",motionThreshold,'%', "Img:",numSav,"      \r"
					if numTriggers > minPixelsChanged:			
						captureCount = 1
				if captureCount > 0:
					camera.resolution = (width, height)
					dtFileStr = time.strftime("/home/pi/Desktop/images/%d-%m-%Y:%H:%M:%S.jpg",time.localtime())
					print "Saved:",dtFileStr
                                        camera.capture_sequence(filenames(),'jpeg',use_video_port=True,quality=92)
					captureCount = captureCount-1
					numSav += 1

        except KeyboardInterrupt:
                print " CTRL-C detected"
                GPIO.cleanup()
                exit()

	finally:
		camera.close()
		print ("Program Terminated")
					

root = Tk()
root.title("Pi Camera")
centre_window(225, 530)


quitButton = Button(root, bg="pink", text="       Quit      ", command=exit)
quitButton.grid(row=0, column=0)

previewButton = Button(root, text="    Preview    ", command=preview)
previewButton.grid(row=1, column=1)

rotateButton = Button(root, text="     Rotate    ", command=rotate)
rotateButton.grid(row=1, column=0)

hflipButton = Button(root, text="      hFlip      ", command=hflip)
hflipButton.grid(row=2, column=0)

vflipButton = Button(root, text="       vFlip      ", command=vflip)
vflipButton.grid(row=2, column=1)

brightUpButton = Button(root, text="   Brighten   ", command=brightUp)
brightUpButton.grid(row=3, column=0)

brightDownButton = Button(root, text="    Darken    ", command=brightDown)
brightDownButton.grid(row=3, column=1)

takeVideoButton = Button(root, text="  Sharpness ", command=sharp)
takeVideoButton.grid(row=4, column=0)

contrastButton = Button(root, text="  Contrast   ", command=contrast)
contrastButton.grid(row=4, column=1)

takeVideoButton = Button(root, text="    Effects    ", command=effects)
takeVideoButton.grid(row=5, column=0)

saturationButton = Button(root, text=" Saturation ", command=sat)
saturationButton.grid(row=5, column=1)

ledButton = Button(root, text="       LED      ", command=led)
ledButton.grid(row=6, column=0)

takeVideoButton = Button(root, text="    Quality    ", command=contrast)
takeVideoButton.grid(row=6, column=1)

favouriteButton = Button(root, text="Set favourites", command=fav)
favouriteButton.grid(row=7, column=0)

demoButton = Button(root, text="     Demo     ", command=demo)
demoButton.grid(row=7, column=1)

w = Scale(root, from_=25, to=75, resolution=1, orient=HORIZONTAL)
w.grid(row=9, column=1)
w.set(camera.brightness)
print "Brightness", camera.brightness

x = Label(root, text="Brightness")
x.grid(row=9, column=0)

y = Scale(root, from_=-50, to=50, resolution=1, orient=HORIZONTAL)
y.grid(row=10, column=1)
y.set(camera.contrast)
print "Contrast", camera.contrast

z = Label(root, text="Contrast")
z.grid(row=10, column=0)

xy = Scale(root, from_=-100, to=100, resolution=1, orient=HORIZONTAL)
xy.grid(row=11, column=1)
xy.set(camera.saturation)
print "Saturation", camera.saturation

xz = Label(root, text="Saturation")
xz.grid(row=11, column=0)

takeStillButton = Button(root, text="   Take still  ", command=still)
takeStillButton.grid(row=20, column=0)

takeVideoButton = Button(root, text="  Take video ", command=vid)
takeVideoButton.grid(row=20, column=1)

yy = Scale(root, from_=0, to=7200, resolution=1, orient=HORIZONTAL)
yy.grid(row=21, column=1)
yy.set(delay)
print "Delay", delay

yz = Label(root, text="Timelapse delay s")
yz.grid(row=21, column=0)

takeStillButton = Button(root, text="Take timelapse", command=lapse)
takeStillButton.grid(row=22, column=0)

takeStillButton = Button(root, text="Motion detect ", command=motion)
takeStillButton.grid(row=22, column=1)

zz = Scale(root, from_=0.5, to=2.5, resolution=0.1, orient=HORIZONTAL)
zz.grid(row=23, column=1)
zz.set(threshPercent)
print "Threshold percentage", threshPercent

zx = Label(root, text="Threshold %")
zx.grid(row=23, column=0)

zoomInButton = Button(root, text = "Zoom in", command = zoomIn)
zoomInButton.grid(row = 24, column = 0)

zoomOutButton = Button(root, text = "Zoom out", command = zoomOut)
zoomOutButton.grid(row = 24, column = 1)


root.mainloop()
