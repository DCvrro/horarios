import csv
from heuristicas import *  # Importa todas las funciones de heuristicas.py

datos = {}
with open('datos.csv', newline='', encoding='iso-8859-1') as archivo_csv:
    lector_csv = csv.DictReader(archivo_csv)
    for fila in lector_csv:
        semestre = int(fila['Semestre'])
        asignaturas = []
        for i in range(1, 6):  # Lee hasta 5 asignaturas
            asignatura = fila[f'Asignatura {i}']
            if asignatura:  # Asegúrate de que la asignatura no esté vacía
                asignaturas.append(asignatura)
        datos[semestre] = {'semestre': semestre, 'asignaturas': asignaturas}
print(datos)

# Aplica las heurísticas para asignar horarios a las pruebas
#semana = h_aleatoria2(datos)
#print(semana)
#for dia,bloques in semana.items():
#    print(dia)
#    count = 0
#    for bloque, ramo in bloques.items():
#        print("Bloque: ",count)
#        count += 1
#        for r in ramo:
#            print(r.getRamo())
        

#resultado_semestre = heuristica_por_semestre(datos)
#resultado_bloques = heuristica_por_bloques_disponibles(datos)
#resultado_restriccion_dia = heuristica_por_restriccion_de_dia(datos)
#resultado_busqueda_local = heuristica_busqueda_local(datos)
