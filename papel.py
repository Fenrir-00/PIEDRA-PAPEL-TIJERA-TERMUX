#!/bin/env python3
import sys
from sys import *
import os 
from os import *
import time
import random
while True:
 try:
  from lolpython import lol_py
  break
 except ModuleNotFoundError:
  os.system("pip install lolpython")

class color:
    morado = '\033[95m'
    blanco = '\033[97m'
    cyan = '\033[96m'
    azul  = '\033[94m'
    verde = '\033[92m' 
    amarillo = '\033[93m' 
    rojo = '\033[91m' 
    fin = '\033[0m'

def banner():
 os.system("clear")
 print(f"""{color.cyan}

██████╗ ██╗███████╗██████╗ ██████╗  █████╗
██╔══██╗██║██╔════╝██╔══██╗██╔══██╗██╔══██╗
██████╔╝██║█████╗  ██║  ██║██████╔╝███████║
██╔═══╝ ██║██╔══╝  ██║  ██║██╔══██╗██╔══██║
██║     ██║███████╗██████╔╝██║  ██║██║  ██║
╚═╝     ╚═╝╚══════╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝""")
 texto ="""
 |=======================================================|
 | Script by              : #FENRIR-00                   |
 | Version                : Version  2.1                 |
 | Follow me on Github    : https://github.com/Fenrir-00 |
 | Contact me on Telegram : @Ritorito1990                |
 ========================================================= """
 lol_py(texto)
 print(f"{color.fin}")

contador = 0
contador1 = 0
contador2 = 0
def piedra():
 global contador
 global contador1
 global contador2
 os.system("clear")
 banner()
 print(f"{color.amarillo}                                                        HAS GANADO " + str(contador))
 print(f"{color.cyan}                                                        HAS EMPATADO " + str(contador1))
 print(f"{color.rojo}                                                        HAS PERDIDO " + str(contador2))
 print(f"{color.morado}        JUEGO PIEDRA PAPEL TIJERA")
 print(f"{color.verde} [1] piedra")
 print(" [2] papel")
 print(" [3] tijera")
 print(f"{color.rojo} [4] restet contador")
 print( " [5] salir")
 vart = (random.choice(['piedra', 'papel', 'tijera']))
 opcionjuego = input(f"{color.cyan}elije una opcion de [1 a 5] >> ")
 if opcionjuego == "1":
  print(f"{color.verde}HAS ELEJIDO PIEDRA")
  if vart == "piedra":
   print(f"{color.cyan}HEMOS EMPATADO")
   time.sleep(2)
   contador1 +=1
   piedra()
  if vart == "papel":
   print(f"{color.rojo}PIERDES JAJAJAJA")
   time.sleep(2)
   contador2 = contador2 +1
   piedra()
  if vart == "tijera":
   print(f"{color.amarillo}FELICIADES HAS GANADO")
   time.sleep(2)
   contador = contador+1
   piedra()
 elif opcionjuego =="2":
  print(f"{color.verde}HAS ELEJIDO PAPEL")
  if vart == "papel":
   print(f"{color.cyan}HEMOS EMPATADO")
   time.sleep(2)
   contador1 = contador1 +1
   piedra()
  if vart == "tijera":
   print(f"{color.rojo}PIERDES JAJAJAJA")
   time.sleep(2)
   contador2 = contador2 +1
   piedra()
  if vart == "piedra":
   print(f"{color.amarillo}FELICIADES HAS GANADO")
   time.sleep(2)
   contador = contador +1
   piedra()
 elif opcionjuego == "3":
  print(f"{color.verde}HAS ELEJIDO TIJERA")
  if vart == "piedra":
   print(f"{color.rojo}PIERDES JAJAJAJA")
   time.sleep(2)
   contador2 = contador2 +1
   piedra()
  if vart == "papel":
   print(f"{color.amarillo}FELICIADES HAS GANADO")
   time.sleep(2)
   contador = contador +1
   piedra()
  if vart == "tijera":
   print(f"{color.cyan}HEMOS EMPATADO")
   time.sleep(2)
   contador1 = contador1 +1
   piedra()
 elif opcionjuego == "4":
  contador = 0
  contador1 = 0
  contador2 = 0
  piedra()
 elif opcionjuego == "5":
  os.system("clear")
  exit
 else :
  print("opcion inconrrecta")
  time.sleep(2)
  piedra()
if __name__ == "__main__":
 piedra()
