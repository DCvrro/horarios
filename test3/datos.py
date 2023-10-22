import csv
#importa todas las funciones de heuristica.py
from heuristicas import *
# Lee los datos desde el archivo CSV
datos = {}
with open('datos.csv', newline='', encoding='utf-8') as archivo_csv:
    lector_csv = csv.DictReader(archivo_csv)
    for fila in lector_csv:
        semestre = fila['Semestre']
        asignaturas = [fila['Asignatura 1'], fila['Asignatura 2'], fila['Asignatura 3'], fila['Asignatura 4'], fila['Asignatura 5']]
        datos[semestre] = {'asignaturas': asignaturas}

# Define las heurísticas (las heurísticas deben estar definidas como se mencionó en la respuesta anterior)

# Aplica las heurísticas para asignar horarios a las pruebas
resultado_aleatorio = heuristica_aleatoria(datos)
resultado_semestre = heuristica_por_semestre(datos)
resultado_bloques = heuristica_por_bloques_disponibles(datos)
resultado_restriccion_dia = heuristica_por_restriccion_de_dia(datos)
resultado_busqueda_local = heuristica_busqueda_local(datos)

# Imprime los resultados o realiza más procesamiento según sea necesario
