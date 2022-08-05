#EJERCICIO NUMERO 7

Destino = ("BJX", "GDL", "JAL")
Pasajeros = []
preferentes = []

#Agregar datos de los pasajeros 
def agregar_pasajeros():
 while True:
    Nombre = input("Ingrese el nombre: ")
    if Nombre != "X":
     ID_INE_IFE = input("Ingrese IDE/INE: ")
     Edad = int(input("Ingrese la edad: "))
     Destino = input("Ingrese IATA del destino: ")
     Cliente_preferente = input("Cliente prefentes: ")
     if Cliente_preferente == "True":
       Cliente_preferente = True
     elif Cliente_preferente == "False":
       Cliente_preferente = False 
     dic = {"Nombre": Nombre, "ID_INE_IFE": ID_INE_IFE, "Edad": Edad, "Destino": Destino, "Cliente_preferente": Cliente_preferente}
     Pasajeros.append(dic)
    else: 
      break

#Listar pasajeros
def Listar_clientes():
  print(Pasajeros)

#Listar clientes preferentes 
def Listar_preferentes():
 for pasajero in Pasajeros:
   if pasajero["Cliente_preferente"] == True:
     preferentes.append(pasajero)
     print(preferentes)
     
#Menú desplegable 

while True:
  print("Menú:\n")
  print("1. Agregar pasajeros:\n")
  print("2. Listar todos los pasajeros:\n")
  print("3. Listar clientes preferentes:\n")
  print("4. Salir:\n")
  Indice_menú = int(input("Selecciona una opción: "))
  if Indice_menú == 1:
    agregar_pasajeros()
  elif Indice_menú == 2:
    Listar_clientes()
  elif Indice_menú == 3:
    Listar_preferentes()
  elif Indice_menú == 4:
    break
   
                                
    
    

 
  
    