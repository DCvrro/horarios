import csv
from heuristicas import *  # Importa todas las funciones de heuristicas.py

# Lee los datos desde el archivo CSV
datos = {}
with open('datos.csv', newline='', encoding='iso-8859-1') as archivo_csv:
    lector_csv = csv.DictReader(archivo_csv)
    for fila in lector_csv:
        semestre = int(fila['Semestre'])      # Extraer el número de semestre del texto, por ejemplo, 'Semestre 1' -> 1
        numero_semestre = int(semestre)
        asignaturas = [fila['Asignatura 1'], fila['Asignatura 2'], fila['Asignatura 3'], fila['Asignatura 4'], fila['Asignatura 5']]
        datos[semestre] = {'semestre': int(numero_semestre), 'asignaturas': asignaturas}
print(datos)




# Aplica las heurísticas para asignar horarios a las pruebas
resultado_aleatorio = heuristica_aleatoria(datos)
resultado_semestre = heuristica_por_semestre(datos)
#resultado_bloques = heuristica_por_bloques_disponibles(datos)
#resultado_restriccion_dia = heuristica_por_restriccion_de_dia(datos)
#resultado_busqueda_local = heuristica_busqueda_local(datos)

# Heurística Aleatoria
print("Resultados de la Heurística Aleatoria:")
for prueba, horario in resultado_aleatorio.items():
    print(f"{prueba}: Día {horario // 4 + 1}, Bloque {horario % 4 + 1}")

# Heurística por Semestre
print("\nResultados de la Heurística por Semestre:")
for prueba, horario in resultado_semestre.items():
    dia, bloque = horario
    print(f"{prueba}: Día {dia + 1}, Bloque {bloque + 1}")

#print("\nResultados de la Heurística por Bloques Disponibles:")
#for prueba, horario in resultado_bloques.items():
#    print(f"{prueba}: Horario {horario} horas")

#print("\nResultados de la Heurística por Restricción de Día:")
#for prueba, horario in resultado_restriccion_dia.items():
#    dia, bloque = horario
#    print(f"{prueba}: Día {dia + 1}, Horario {bloque} horas")

#print("\nResultados de la Heurística de Búsqueda Local:")
#for prueba, horario in resultado_busqueda_local.items():
#    print(f"{prueba}: Horario {horario} horas")
#