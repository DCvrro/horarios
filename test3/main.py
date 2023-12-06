from heuristicas import * # Importa todas las funciones de heuristicas.py
import csv

def leerRamos():
    datos = {}
    with open('datos.csv', newline='', encoding='iso-8859-1') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        for fila in lector_csv:
            semestre = int(fila['Semestre'])
            asignaturas = []
            for i in range(1, 6):
                ramo = fila[f'Asignatura {i}']
                if ramo:
                    asignaturas.append(ramo)
            datos[semestre] = {'semestre': semestre, 'asignaturas': asignaturas}
    return datos

    
#funcion main
if __name__ == '__main__':
#Aqui ejecutaremos todas las heuristicas e imprimiremos los resultados sin modificaciones
    datos = leerRamos()
    #print(datos)
    resultado = ""
    valores=""
    #print(datos)
    h1 = h_aleatoria2(datos)
    h2 = heuristica_3(datos)
    
    for dato in datos:
        print(datos[dato.getRamo()])

    resultado = ""

    ramos_totales = 0
    resultado = resultado + "----"*30 + "\n"
    valores = valores + "----"*30 + "\n"
    resultado +="Heuristica 1\n"
    valores +="Heuristica 1\n"
    resultado = resultado + "----"*30 + "\n"

    for dia, bloques in h1.items():
        sem_dia = []
        resultado += str(dia) + "\n"
        valores +=str(dia) + " "
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
        valores += str(len(sem_dia)) + " "
        resultado += f"Total de ramos para el dia {dia}: {ramos}\n"
        resultado += f"Semestres evaluados el dia {dia}: {set(sem_dia)}\n"
        resultado = resultado + "----"*30 + "\n"
    resultado += f"Total de ramos: {ramos_totales} de 50\n"
    valores += f"\ntotal {ramos_totales}\n"
    resultado = resultado + "----"*30 + "\n"
    
    ramos_totales = 0 
    resultado +="Heuristica 2\n"
    valores +="Heuristica 2\n"
    resultado = resultado + "----"*30 + "\n"

    for dia, bloques in h2.items():
        sem_dia = []
        resultado += str(dia) + "\n"
        valores +=str(dia) + " "
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
        valores += str(len(sem_dia)) + " "
        resultado += f"Total de ramos para el dia {dia}: {ramos}\n"
        resultado += f"Semestres evaluados el dia {dia}: {set(sem_dia)}\n"
        resultado = resultado + "----"*30 + "\n"
    resultado += f"Total de ramos: {ramos_totales} de 50\n"
    valores += f"\ntotal {ramos_totales}\n"
    resultado = resultado + "----"*30 + "\n"



    with open("resultados.txt", "w") as archivo:
        archivo.write(resultado)
    with open("valores.txt", "w") as archivo:
        archivo.write(valores)