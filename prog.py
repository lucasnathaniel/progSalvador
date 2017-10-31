from socket import socket, AF_INET, SOCK_STREAM
import re

sock = socket(AF_INET, SOCK_STREAM)

sock.connect(("138.197.10.170",9008))
print('connectou!')
print(sock.recv(2048).decode())
sock.send("start".encode())

print(sock.recv(1024).decode()) #iniciando
contador = 1

#COMPUTADOR COMEÇA PRIMEIRO:
while(contador <= 20):
	print("\033[01;93mDesafio numero ", contador)
	print("\033[0m")
	
	mensagem = sock.recv(36).decode() #vez do pc
	computador1 = int(re.findall(": \d+", mensagem)[0][2:])
	print(mensagem)
	print(sock.recv(10).decode()) #quebra de linha
	print(sock.recv(35).decode()) #sua vez
	
	if(computador1 == 5):
		eu1 = 6
	else:
		eu1=5

	sock.send(str(eu1).encode())
	print(sock.recv(40).decode()) #hacker escolheu...
	

	mensagem = sock.recv(36).decode() #vez do pc
	computador2 = int(re.findall(": \d+", mensagem)[0][2:])
	print(mensagem)
	
	print(sock.recv(35).decode()) #sua vez
	eu2 = 15-(computador1+computador2)
	sock.send(str(eu2).encode())
	print(sock.recv(40).decode()) #hacker escolheu...
	

	mensagem = sock.recv(36).decode() #vez do pc
	computador3 = int(re.findall(": \d+", mensagem)[0][2:])
	print(mensagem)
	print(sock.recv(35).decode()) #sua vez
	
	if(computador3 != 15-(eu1+eu2)): #se o pc for burro
		eu3 = 15-(eu1+eu2)
		pcburro = True
	else:
		if(computador3 == 7 or computador3 == 3):
			if(computador1 == 5):
				eu3 = 3
			else:
				eu3 = 1
		else:
			eu3 = 3
		pcburro = False
	
	sock.send(str(eu3).encode())
	
	if(pcburro):
		continue
	
	print(sock.recv(40).decode()) #hacker escolheu...
	

	mensagem = sock.recv(36).decode() #vez do pc
	computador4= int(re.findall(": \d+", mensagem)[0][2:])
	print(mensagem)
	print(sock.recv(35).decode()) #sua vez

	if(computador4 != 9):
		eu4 = 9
		if(computador4 != 1):
			pcburro = True
	else:
		if(computador1 == 8 or computador1 == 4): #se tiver no lado direito
			eu4 = 2
		else:
			eu4 = 4
		pcburro = False

	sock.send(str(eu4).encode())

	if(pcburro):
		continue

	print(sock.recv(40).decode()) #hacker escolheu...
	

	print(sock.recv(36).decode()) #vez do pc
	print(sock.recv(35).decode()) #EMPATOU
	print(sock.recv(35).decode())

	contador +=1


#VOCÊ COMEÇA PRIMEIRO:

print(sock.recv(35).decode()) #sua vez

eu1 = 6 

sock.send(str(eu1).encode())

print(sock.recv(40).decode()) #hacker escolheu...
mensagem = sock.recv(36).decode() #vez do pc
computador1 = int(re.findall(": \d+", mensagem)[0][2:])
print(mensagem)


print(sock.recv(35).decode()) #sua vez

if(computador1 == 5):
	eu2 = 4
if(computador1 == 7):
	eu2 = 8
if(computador1 == 1):
	eu2 = 2

sock.send(str(eu2).encode())
print(sock.recv(40).decode()) #hacker escolheu...
mensagem = sock.recv(36).decode() #vez do pc
computador2 = int(re.findall(": \d+", mensagem)[0][2:])
print(mensagem)


print(sock.recv(35).decode()) #sua vez

if(eu2 == 4 and computador2 == 8):
	eu3 = 2
if(eu2 == 4 and computador2 == 2):
	eu3 = 8

sock.send(str(eu3).encode())
print(sock.recv(40).decode()) #hacker escolheu...
mensagem = sock.recv(36).decode() #vez do pc
computador3 = int(re.findall(": \d+", mensagem)[0][2:])
print(mensagem)


print(sock.recv(35).decode()) #sua vez

if(computador3 == 7):
	eu4 = 9
if(computador3 == 9):
	eu4 = 7

sock.send(str(eu4).encode())

print(sock.recv(40).decode()) #GANHEI
print(sock.recv(35).decode())

print(sock.recv(2048).decode())
sock.close()