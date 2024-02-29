# Crear una matriz 3D para almacenar datos de temperaturas
import random

ciudad = ["Lago Agrio", "Cuenca", "Ambato"]

dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Sábado", "Domingo" ]

semanas = ["semana1", "semana2", "semana3","semana4"]

temperatura = [[[random.randint(15, 80) for _ in dias] for _ in semanas] for _ in ciudad]

for ciudad, temps_ciudad in zip(ciudad, temperatura):

    print(f"Promedio de temperaturas para {ciudad}:  ")

    for semana, temps_semana in zip(semanas, temps_ciudad):

        promedio = sum(temps_dia for temps_dia in temps_semana) / len(temps_semana)

        print(f"{semana}: {promedio:.2f} grados Celsius")
    print()

