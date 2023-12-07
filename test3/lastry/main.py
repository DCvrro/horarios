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

def Hiperheuristica(resultados):
    #Aqui se analizarán todos los resultados obtenidos por las heuristicas
    #Verificnado cual es el mejor horario en base a diferentes puntos.
    heuristica = 0
    ramos = [] # Cuantos ramos considero cada heuristica. 
    sem_heuristicas = []
    sem_rep_xheuristica = []
    i = 1
    y = 0
    for heuristica in resultados:
        #Aqui empiezo a ver los resultados, uno por uno.
        count_ramos = 0 #Contamos cuantos ramos contó cada heuristica y lo guardamos en un arreglo ramos. 
        sem_sem = []
        sem_sem_reps = []
        for dias in resultados[heuristica]:
            sem_dia = [] #Vemos cuantos semestre diferentes tomó por dia. 
            sem_dia_reps = []
            for bloque in resultados[heuristica][dias]:
                for ramo in resultados[heuristica][dias][bloque]:
                    #Guardo cuan diferentes ramos hay por dia en relacion a los semestres. 
                    if ramo[1] not in sem_dia:
                        sem_dia.append(ramo[1])
                    else:
                        sem_dia_reps.append(ramo[1])
                    count_ramos += 1
            sem_sem_reps.append(sem_dia_reps)
            sem_sem.append(sem_dia)

        ramos.append(count_ramos)
        sem_heuristicas.append(sem_sem)
        print("\nHeuristica : ", i ,"")
        print("Ramos: ", count_ramos)
        print("Semestres de la semana: ", sem_sem)
        k = 0
        for sem in sem_sem:
            #veo cuantos ramos hay por dia.
            if k == 0:
                print("Lunes:", len(sem), end=" ")
            elif k == 1:
                print("Martes:", len(sem), end=" ")
            elif k == 2:
                print("Miercoles:", len(sem), end=" ")
            elif k == 3:
                print("Jueves:", len(sem), end=" ")
            elif k == 4:
                print("Viernes:", len(sem), end=" ")
            k += 1
        print("\n Semestres repetidos: ", sem_sem_reps)
        i += 1
                    
                   
    return heuristica
                    
if __name__ == '__main__':
    datos = leerRamos()
    resultados = {}
    horario = create_horario()
    print("Horario:\n",horario)
    print("Datos:\n",datos)
    
    resultados[1] = h1(datos,horario)
    #print("Heuristica 1:\n", resultados[1],"\n")
    
    horario = create_horario()
    resultados[2] = h2(datos,horario)
    #print("Heuristica 2:\n", resultados[2],"\n")
    
    datos= leerRamos()
    horario = create_horario()
    resultados[3] = h3(datos,horario)
    #print("Heuristica 3:\n", resultados[3],"\n")
    
    a = Hiperheuristica(resultados)