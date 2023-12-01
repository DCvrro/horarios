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
resultado = ""
semana_h1 = h_aleatoria2(datos)
#semana_h2 = h_aleatoria3(datos)
ramos_totales = 0
resultado = resultado + "----"*30 + "\n"
resultado +="Heuristica 1\n"
resultado = resultado + "----"*30 + "\n"

for dia, bloques in semana_h1.items():
    sem_dia = []
    resultado += str(dia) + "\n"
    count = 0
    ramos = 0
    for bloque, ramo in bloques.items():
        resultado += '\n'
        resultado += f"Bloque: {count}\n"
        count += 1
        for r in ramo:
            resultado += str(r.getRamo()) + "\n"
            sem_dia.append(r.getSemestre())
            ramos += 1
            ramos_totales += 1
    resultado = resultado + "----"*30 + "\n"
    resultado += f"Total de ramos para el dia {dia}: {ramos}\n"
    resultado += f"Semestres evaluados el dia {dia}: {set(sem_dia)}\n"
    resultado = resultado + "----"*30 + "\n"
resultado += f"Total de ramos: {ramos_totales} de 50\n"
resultado = resultado + "----"*30 + "\n"


with open("resultados.txt", "w") as archivo:
    archivo.write(resultado)

