
Pasajeros = []
Destinos = ['BJX', 'GDL', 'JAL']

while True: 
  Solicitar_nombre = input('Nombre: ')
  if Solicitar_nombre != "X":
    Solicitar_edad = int(input('Edad: '))
    Solicitar_destino = input('IATA destino: ')
    Pasajeros.append((Solicitar_nombre, Solicitar_edad, Solicitar_destino))
  else:
    break

pasajeros_totales = []
edad_promedio = []

for Solicitar_destino in Destinos:
  total_pasajeros = 0
  total_edad = 0
  for pasajero in Pasajeros:
    if Solicitar_destino == pasajero[2]:
      total_pasajeros += 1
      total_edad += pasajero[1]
  pasajeros_totales.append((Solicitar_destino, total_pasajeros))
  if total_pasajeros > 0:
    edad_promedio.append((Solicitar_destino, total_edad/total_pasajeros))

    
print(pasajeros_totales)
print(edad_promedio)