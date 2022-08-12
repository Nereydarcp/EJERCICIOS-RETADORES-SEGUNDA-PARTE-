Destino = ("BJX", "GDL", "JAL")
Clientes = {45471:["Luis Perez", 45, "BJX", True], 8944411:["Fernanda Garcia", 25, "JAL", True], 15223:["Alejandra Ortiz", 33, "JDL", True]}
Pasajeros = []
preferentes = {}

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
     Cliente = [Nombre, Edad, Destino, Cliente_preferente]
     Clientes[ID_INE_IFE] = Cliente
   else: 
       break     

#Listar clientes 
def listar_clientes():
  print(Clientes)
  
def listar_preferentes():
  for key, Cliente in Clientes.items():
    if Cliente[-1] == True:
     preferentes[key] = Cliente 
    print(preferentes)
  
def borrar_cliente():
  ID_borrar = int(input("¿Cuál es el ID que desea borrar: "))
  Clientes.pop(ID_borrar)
  print(Clientes )
  
def edad_promedio():
  sumatoria = 0
  for Cliente in Clientes.values():
    sumatoria += Cliente[1]
  edad_promedio = sumatoria/len(Clientes)
  print(edad_promedio)

def edad_promedio_clientes_preferentes():
  sumatoria = 0
  for preferente in preferentes.values():
    sumatoria += preferente[1]
    if len(preferentes)>0:
      edad_promedio = sumatoria/len(preferentes)
      print(edad_promedio)
    else:
      print("No hay registro de clientes preferentes")
 
  
while True:
  print("Menú:\n")
  print("1.  Añadir nuevos clientes:\n")
  print("2. Listar todos los clientes:\n")
  print("3. Listar clientes preferentes:\n")
  print("4. Eliminar un cliente mediante ID del INE:\n")
  print("5. Edad promedio de todos los clientes:\n")
  print("6. Edad promedio de clientes preferentes:\n")
  print("7. Salir:\n")
  Indice_menú = int(input("Selecciona una opción: "))
  if Indice_menú == 1:
    agregar_pasajeros()
  elif Indice_menú == 2:
    listar_clientes()
  elif Indice_menú == 3:
    listar_preferentes()
  elif Indice_menú == 4:
    borrar_cliente()
  elif Indice_menú == 5:
    edad_promedio()
  elif Indice_menú == 6:
    edad_promedio_clientes_preferentes()
  elif Indice_menú == 7:
    break