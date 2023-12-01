import random
import numpy as np
class asignatura:
    def __init__(self,ramo, semestre):
        self.ramo = ramo
        self.semestre = semestre
    def getRamo(self):
        return self.ramo
    
    def getSemestre(self):
        return self.semestre
    
    def setRamo(self, ramo):
        self.ramo = ramo
        
    def setSemestre(self, semestre):
        self.semestre = semestre
    
    def getData(self):
        return self.ramo, self.semestre

import numpy as np

def h_aleatoria3(datos):
    np.random.seed()
    dias = np.array(['1', '2', '3', '4', '5'])
    semana = [[], [], [], [], []]
    horario = {}
    for dia_ in dias:
        horario[dia_] = {}
    bloques = 4
    asignaturas = []
    for sem in datos:
        for asig in datos[sem]['asignaturas']:
            tmp = asignatura(asig, sem)
            asignaturas.append(tmp)
    for dia_ in horario:
        for i in range(bloques):
            horario[dia_][i + 1] = []

    #print(horario)
    while asignaturas:
        #print("Asignaturas: ", len(asignaturas))
        dia = np.random.choice(dias)  # Usando np.random.choice en lugar de random.choice
        #print("DIAAAAA: ", dia)
        bloques = np.random.choice(list(range(1, 5))).__int__()
        tmp = np.random.choice(asignaturas)
        semTmp = tmp.getSemestre()
        #print("Dia: ", dia, "Bloque: ", bloques, "Semestre: ", semTmp)
        if semTmp not in semana[int(dia) - 1]:
            horario[dia][bloques].append(tmp)
            semana[int(dia) - 1].append(semTmp)
            asignaturas.remove(tmp)

        elif semTmp in semana[int(dia) - 1] and len(semana[int(dia) - 1]) < 10:
            validar = True
            count = 0
            while validar:
                if not asignaturas:
                    validar = False
                    break
                tmp_ = np.random.choice(asignaturas)
                semTmp_ = tmp_.getSemestre()
                if semTmp_ not in semana[int(dia) - 1]:
                    horario[dia][bloques].append(tmp_)
                    semana[int(dia) - 1].append(semTmp_)
                    asignaturas.remove(tmp_)
                    validar = False
                    break
                elif count == 10:
                    validar = False
                    #print("No se pudo asignar")
                    break
                else:
                    count += 1
                    validar = True
    #print(len(asignaturas))
    return horario
def h_aleatoria2(datos):
    dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']
    horario = {}
    for dia in dias:  #con esto asigno los dias de la semana de la libreta
        horario[dia] = {}
    bloques =  4
    #creamos un arreglo con todas las asignaturas
    asignaturas = []
    for sem in datos:

        for asig in datos[sem]['asignaturas']:
            tmp = asignatura(asig, sem)
            asignaturas.append(tmp)
    for dias in horario:
        #Creamos los bloques
        for i in range(bloques):
            horario[dias][i+1] = []

    for dias in horario:
        semDia = []
        for bloque in horario[dias]:
            for i in range(0,4):
                if asignaturas == []:
                    break
                tmp = random.choice(asignaturas)
                semTmp = tmp.getSemestre()
                if semTmp not in semDia:
                    horario[dias][bloque].append(tmp)
                    semDia.append(semTmp)
                    asignaturas.remove(tmp)
                elif semTmp in semDia and len(semDia) < 10:
                    validar = True
                    while(validar):
                        if asignaturas == []:
                            break
                        tmp_ = random.choice(asignaturas)
                        semTmp_ = tmp_.getSemestre()
                        if semTmp_ not in semDia:
                            horario[dias][bloque].append(tmp_)
                            #print("Dia:", dias , "bloque: ", bloque , "Semestres: ", semDia, "Asignaturas: ", len(asignaturas))
                            semDia.append(semTmp_)
                            asignaturas.remove(tmp_)
                            validar = False
                            break
                        else:
                            validar = True
                #print("Dia:", dias , "bloque: ", bloque , "Semestres: ", semDia, "Asignaturas: ", len(asignaturas))

    return horario
#heuristica por orden de malla.
def  heuristica_3(datos):
    dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']
    horario = {}
    for dia in dias:  #con esto asigno los dias de la semana de la libreta
        horario[dia] = {}
    bloques =  4
    asignaturas = []
    for sem in datos:
        for asig in datos[sem]['asignaturas']:
            tmp = asignatura(asig, sem)
            asignaturas.append(tmp)
    for dias in horario:
        #Creamos los bloques
        for i in range(bloques):
            horario[dias][i] = []
    
    for i in range(0,4):
        for dias in horario:
            if asignaturas == []:
                break
            else: 
                horario[dias][i].append(asignaturas.pop())
                print(asignaturas)
 
    return horario

def heuristica_4(datos):
    probabilidades = {
       'Algebra y Geometría': 0.05,
       'Clculo 1': 0.05,
       'Química': 0.05,
       'Programacion': 0.05,
       'Comunicacion para la Ingeniera': 0.05,
       'lgebra Lineal': 0.04,
       'Clculo 2': 0.04,
       'Mecnica': 0.04,
       'Programacion Avanzada': 0.04,
       'CFG': 0.04,
       'EDO': 0.03,
       'Clculo 3': 0.03,
       'Calor y Ondas': 0.03,
       'Estructura de Datos y Algoritmos': 0.03,
       'Redes de Datos': 0.03,
       'Probabilidad y Estadsticas': 0.02,
       'Electrnica y Electrotecnia': 0.02,
       'Electricidad y Magnetismo': 0.02,
       'Bases de Datos': 0.02,
       'Desarrollo Web y Mvil': 0.02,
       'Optimizacin': 0.015,
       'Taller de Redes y Servicios': 0.015,
       'Proyecto en TICs 1': 0.015,
       'Bases de Datos Avanzadas': 0.015,
       'Contabilidad y Costos': 0.015,
       'Arquitectura y Organizacin de Computadores': 0.015,
       'Seales y Sistemas': 0.015,
       'Sistemas Operativos': 0.015,
       'Gestin Organizacional': 0.01,
       'Sistemas Distribuidos': 0.01,
       'Comunicaciones Digitales': 0.01,
       'Ingeniera de Software': 0.01,
       'Introduccin a la Economa': 0.01,
       'Tecnologas Inalmbricas': 0.01,
       'Criptografa y Seguridad en Redes': 0.01,
       'IA': 0.01,
       'Evaluacin de Proyectos TIC': 0.01,
       'Electivo Profesional': 0.005,
       'Arquitecturas Emergentes': 0.005,
       'Arquitectura de Software': 0.005,
       'Data Science': 0.005,
       'Proyecto en TICS 2': 0.005,
    }   
    dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']
    horario = {}
    for dia in dias:  #con esto asigno los dias de la semana de la libreta
        horario[dia] = {}
    bloques =  4
    asignaturas = []
    for sem in datos:
        for asig in datos[sem]['asignaturas']:
            tmp = asignatura(asig, sem)
            asignaturas.append(tmp)
    for dias in horario:
        #Creamos los bloques
        for i in range(bloques):
            horario[dias][i] = []
    for dias in horario:
        for dias in bloques:
            if asignaturas == []:
                break
            else: 
                horario[dias][i].append(asignaturas.pop())
    return horario