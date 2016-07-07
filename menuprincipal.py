#Programa de prueba (examen)
print("Programa cajero Banco lA SARITA...")
print( )
#Aldo
def menu():
  nnmobre()
  ndni()
  nedad()
  opciones()
  
def opciones():
  os.system("clear")
  while(1):
    try:
      print("Banco Sarita")
      print("1.- Reporte")
      print("2.- Retiro /deposito")
      print("3.- Prestamo")
      print("4.- Salir")
      print("Ingrese una opcion ")
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
        print("1.-Deposito")
        print("2.-Retiro")
        z=input
        z=int(z)
        while (x<0 or x>2):
          print("Ingrese correctamente de 1 a 2")
          z=input
          z=int(z)
        break
      except ValueError:
        print("Ingrese correctamente una opcion valida")
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
      print("Ingrese su Edad ")
      edad=input()
      edad=int(edad)
      while(edad<=0 or edad>150):
        print("Ingrese su Edad Correctamente")
        edad=input()
        edad=int(edad)
      break
    except ValueError:
      print("Ingrese Su Edad Correctamente")
      
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
     
