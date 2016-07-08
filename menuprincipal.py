#Programa de prueba (examen)
import time,os,sys
print("Programa cajero Banco lA SARITA...")
print( )
#Aldo
def menu():
  nnombre()
  ndni()
  nedad()
  opciones()
  
def opciones():
  os.system("clear")
  while(1):
    try:
      print("\t\t*****Banco Sarita*****")
      print("\t1.- Reporte")
      print("\t2.- Retiro /deposito")
      print("\t3.- Prestamo")
      print("\t4.- Salir")
      print("Ingrese una opcion: ")
      x=input()
      x=int(x)
      while (x<0 or x>4):
        print("Ingrese correctamente la opcion de 1 a 4:")
        x=input()
        x=int(x)
      break
    except ValueError:
      print("Error opcion invalida vuelva a intentar")
  if(x==1):
    nreporte()
    opciones()
  elif (x==2):
    while (1):
      try:
        print("\t1.-Deposito")
        print("\t2.-Retiro")
        z=input
        z=int(z)
        while (x<0 or x>2):
          print("Ingrese correctamente de 1 a 2: ")
          z=input
          z=int(z)
        break
      except ValueError:
        print("Ingrese correctamente una opcion valida: ")
    if (z==1):
      ndeposito()
      opciones()
    elif (z==2):
      nretiro()
      opciones()
  elif (x==3):
    nprestamo()
    opciones()
  elif (x==4):
    sys.exit()
  

#Julio
def verificar(x):
  for c in x:
    if((ord(c)<65 or ord(c)>90) and (ord(c)<97 or ord(c)>122) and (ord(c)!=32)):
      return False
  return True

def nnombre():
  global nombre
  print("Ingrese su Nombre")
  nombre=input()
  while(not verificar(nombre)):
    print("Verifique Error en Nombre")
    nombre=input()
    
def nedad():
  global edad
  while(1):
    try:
      print("Ingrese su Edad: ")
      edad=input()
      edad=int(edad)
      while(edad<=0 or edad>150):
        print("Ingrese su Edad Correctamente: ")
        edad=input()
        edad=int(edad)
      break
    except ValueError:
      print("Ingrese Su Edad Correctamente: ")
#kevin
def nreporte():
  os.system("clear")
  print("*********reporte********")
  print("NOMBRE    :",nombre)
  print("DNI       :",dni)
  print("EDAD      :",edad)
  print("TIPO      :", cambio,"%",)
  print("MONTO DE FONDO",fondo,"S/")
  time.sleep(4)
def ndni():
  global dni
  global cambio
  dat_dni=""
  while(1):
    try:
      print("Ingrese su DNI: ")
      dni=input()
      dni=int(dni)
      while(len(str(dni))!=8):
        print("Ingrese de un tamaño de 8 Digitos: ")
        dni=input()
        dni=int(dni)
      data_dni=str(dni)
      break
    except ValueError:
      print("Ingrese Correctamente su DNI: ")
  if (data_dni[0:2] == "01"):
    cambio=4
  elif(data_dni[0:2]=="29"):
    cambio=4
  else:
    cambio=2
def nfondo():
  global fondo
  while(1):
    try:
      print("Ingrese su fondo: ")
      fondo=input()
      fondo=int(fondo)
      while(fondo<0):
        print("Ingrese Correctamente: ")
        fondo=input()
        fondo=int(fondo)
      break
    except ValueError:
      print("Ingrese Correctamente: ")
  
#christian
def nretiro():
  os.system("clear")
  global fondo
  print("CUENTA CON UN SALDO DE",fondo,)
  global retiro
  while(1):
    try:
      print("Ingrese su monto de retiro: ")
      retiro=input()
      retiro=int(retiro)
      while(retiro<0 or retiro>fondo):
        print("Ingrese correctamente, no tiene saldo")
        retiro=input()
        retiro=int(retiro)
      break
    except ValueError:
      print("Ingrese correctamente")
      
  fondo=fondo - retiro
  
  print()
  print("**********Banco SARITA**********")
  print("Nombre         :",nombre)
  print("DNI            :",dni)
  print("Saldo total    :",fondo)
  print("Retiro         :",retiro)
  time.sleep(4)
  #jonathan
def ndeposito():
  os.system("clear")
  global deposito
  global fondo
  print("Cuenta con un saldo de",fondo,)
  while(1):
    try:
      print("ingrese su monto de deposito")
      deposito=input()
      deposito=int(deposito)
      while(deposito<0):
        deposito=input()
        deposito=int(deposito)
      break
    except ValueError:
      print("ingrese correctamente")
  fondo=fondo+deposito
  
  print("************BANCO SARITA******")
  print("NOMBRE           :",nombre)
  print("DNI              :",dni)
  print("SALDO TOTAL      :",fondo)
  print("DEPOSITO         :",deposito)
  time.sleep(4)
def nprestamo():
  os.system("clear")
  global prestamo
  while(1):
    try:
      print("ingrese su prestamo")
      prestamo=input()
      prestamo=int(prestamo)
      while(prestamo<0):
        print("ingrese correctamente su prestamo")
        prestamo=input()
        prestamo=int(prestamo)
      break
    except ValueError:
      print("ingrese correctamente")
  nmeses()
  
#wil
def nmeses():
  global meses
  while(1):
    try:
      print("Ingrese la cantidad de meses: ")
      meses= input()
      meses = int(meses)
      while (prestamo < 0):
        print("Ingrese correctamente la cantidad de meses")
        meses = input()
        meses = int(meses)
      break
    except ValueError:
      print("Ingrese correctamente")
  iprestamo()
def iprestamo():
  prestamo = prestamo + ( prestamo*cambio/100*meses )
  mest = prestamot / meses
  print("prestamo total",prestamot,"S/")
  print("prestamo mensual", mest, "S/")
  time.sleep(4)
  
menu()
