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


#reviso si existe una asignatura del mismo semestre en el mismo dia