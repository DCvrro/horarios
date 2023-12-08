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


def ubicacion_maximos(arreglo):
    max1 = float('-inf')
    max2 = float('-inf')
    index1 = -1
    index2 = -1

    for i, num in enumerate(arreglo):
        if num > max1:
            max2 = max1
            index2 = index1
            max1 = num
            index1 = i
        elif num > max2 and num != max1:
            max2 = num
            index2 = i

    if index2 == -1:
        return [index1]
    else:
        return [index1, index2]


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

    ramos = [] # Cuantos ramos considero cada heuristica. 
    sem_heuristicas = []
    sem_rep_xheuristica = []
    i = 1
    y = 0
    cant_heu = len(resultados)  #Cantidad de heuristicas que se usaron.
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
        sem_rep_xheuristica.append(sem_sem_reps)
    print("Ramos: ", ramos)
    print("Semestres: ", sem_heuristicas)
    print("Semestres repetidos: ", sem_rep_xheuristica)

    #Aqui empieza el analisis de datos para ver cual es el mejor horario.
    #Primero revisamos por cantidad de ramos considerados por horario. 

    #Si tiene considerado los 50 ramos, sumamos 5 puntos.
    puntajes = {}
    #el diccionario almacenará
    # Cada llave será una heuristica
    # Luego cada llave tendrá un arreglo con los puntajes de cada heuristica.   
    # 1. Cantidad de ramos considerados.
    # 2. Cantidad de semestres considerados.
    # 3. Cantidad de semestres repetidos.
    # Luego se suman los puntajes y se ve cual es el mejor horario.
    # Lo retorna nuestra hiperheuristica.
    
    for i in range(cant_heu):
        puntajes[i+1] = []
        if ramos[i] == 50:
            puntajes[i+1].append(5)
        elif ramos[i] < 50 and ramos[i] > 45:
            puntajes[i+1].append(2)
        elif ramos[i] < 45 and ramos[i] > 40:
            puntajes[i+1].append(1)
        else :
            puntajes[i+1].append(0)

    #Ahora revisamos por cantidad de semestres diferentes considerados por dia.
    #Si tiene considerado los 10 semestres en todos los dias, suma 5 puntos.
    #Si tiene considerado los 10 semestres en 4 dias, suma 3 puntos.
    #Si tiene considerado los 10 semestres en 3 dias, suma 2 puntos.
    #Si tiene considerado los 10 semestres en 2 dias, suma 1 puntos.
    #Cualquier otro caso se considera 0 puntos.
    
    for i in range(cant_heu):
        count = 0
        for dias in sem_heuristicas[i]:
            if len(dias) == 10:
                count += 1
        if count == 5:
            puntajes[i+1].append(5)
        elif count == 4:
            puntajes[i+1].append(3)
        elif count == 3:
            puntajes[i+1].append(2)
        elif count == 2:
            puntajes[i+1].append(1)
        else:
            puntajes[i+1].append(0)

    #Ahora revisamos por cantidad de semestres repetidos considerados por dia.
    #Si tiene un ramo o más repetido en todos los dias, suma -1 puntos.
    #Si tiene un ramo o más repetido en 4 dias, suma 0 puntos.
    #Si tiene un ramo o más repetido en 3 dias, suma 1 puntos.
    #cualquier otro caso se considera 2 puntos.
    

    for i in range(cant_heu):
        count = 0
        for dias in sem_rep_xheuristica[i]:
            if len(dias) > 0:
                count += 1
        if count == 5:
            puntajes[i+1].append(-1)
        elif count == 4:
            puntajes[i+1].append(0)
        elif count == 3:
            puntajes[i+1].append(1)
        else:
            puntajes[i+1].append(2)

    #Ahora sumamos los puntajes y vemos cual es el mejor horario.
    #El mejor horario es el que tiene mayor puntaje.
    #Entregaremos el numero de la heuristica que tiene el mejor horario.
    #Si hay empate, se entregan ambos numeros de heuristica.Sin embargo, se destaca el resultado del tercer puntaje. 
            
    print("Puntajes: ", puntajes)

    #Ahora vemos cual es el mejor puntaje.
    #Si hay empate, se destaca el tercer puntaje.
    
    puntajes_totales = []

    for heuristicas in puntajes:
        punt_temp = 0
        for valores in puntajes[heuristicas]:
            punt_temp += valores
        puntajes_totales.append(punt_temp)
    
    for i in range(len(puntajes_totales)):
        print("Heuristica", i+1, ":", puntajes_totales[i])
    
    tops = ubicacion_maximos(puntajes_totales)

    if len(tops) == 1:
        heuristica = tops[0] + 1
        return heuristica
    else:
        heuristica = tops[0] + 1 , tops[1] + 1
        return heuristica

    
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

    if type(a) == tuple:
        print("Los mejores horarios son los de las heuristicas", a[0], "y", a[1])
        print("Con los siguientes horarios:")
        print("Heuristica", a[0], ":\n", resultados[a[0]],"\n")
        print("Heuristica", a[1], ":\n", resultados[a[1]],"\n")
    else:
        print("El mejor horario es el de la heuristica", a)
        print("Con el siguiente horario:")
        print("Heuristica", a, ":\n", resultados[a],"\n")
