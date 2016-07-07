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
