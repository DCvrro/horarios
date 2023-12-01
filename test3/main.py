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
def main():
    #Aqui ejecutaremos todas las heuristicas e imprimiremos los resultados sin modificaciones
    datos = leerRamos()
    print(datos)
    resultado = ""
    #print(datos)
    h1 = h_aleatoria2(datos)
    h2 = heuristica_1(datos)
    h3 = heuristica_2(datos)

    print("Heuristica 3\n",h3)
#funcion main
if __name__ == '__main__':
    main()