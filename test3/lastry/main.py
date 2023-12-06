import csv
import random
import numpy
from heuristicas import *

def leerRamos():
    datos ={} 
    with open('datos.csv', newline='', encoding='utf-8') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        for fila in lector_csv:
            semestre = int(fila['Semestre'])
            ramos_semestre = []
            for i in range(1,6):
                asignatura = fila[f'Asignatura {i}']
                datos[semestre] = ramos_semestre.append(asignatura)
            datos[semestre] = ramos_semestre
            
    return datos

def create_horario():
    dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']
    horario= {}
    for d in dias: 
        horario[d] = {}
        
    bloques = 4
    for dias in horario:
        for i in range(bloques):
            horario[dias][i] = []
    return horario
    
                    
if __name__ == '__main__':
    datos = leerRamos()
    
    horario = create_horario()
    print("Horario:\n",horario)
    print("Datos:\n",datos)
    
    print("Heuristica 1:\n", h1(datos,horario),"\n")
    
    horario = create_horario()
    print("Heuristica 2:\n", h2(datos,horario),"\n")
    
    datos= leerRamos()
    horario = create_horario()
    print("Heuristica 3:\n", h3(datos,horario),"\n")