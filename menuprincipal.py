#Programa de prueba (examen)
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
    
