#Programa de prueba (examen)
print("Programa cajero Banco lA SARITA")
print()
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
   
    
     
     
