import random
#Heuristica 1: Horario aleatorio, en orden de dia y bloque.
def h1(datos,horario):
    data = []
    for sem in datos:
        for asig in datos[sem]:
            tmp = [asig, sem]
            data.append(tmp)
    
    while(data):
        for dia in horario:
            for bloques in horario[dia]:
                for i in range(4):
                    if data == []:
                        break
                    tmp = random.choice(data)
                    horario[dia][bloques].append(tmp)
                    data.remove(tmp)
    return horario
#Heuristica 2: horario por orden de malla
def h2(datos,horario):
    for semestre in datos:
        for dia in horario:
            for bloque in horario[dia]:
                if len(horario[dia][bloque]) < 3:
                    if datos[semestre] == []:
                        break
                    else:
                        tmp = random.choice(datos[semestre])
                        tmp2 = [tmp, semestre]
                        horario[dia][bloque].append(tmp2)
                        datos[semestre].remove(tmp)
    return horario

#Heurística 5: Horario por orden, pero de a un incremento
def h3(datos,horario):
    dias_semana = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']
    dia = 0
    bloque = 0
    for i in range(0,10):
        for ramos in datos[i+1]:
            if dia == 5:
                dia = 0
                bloque = bloque + 1
            if bloque == 4:
                bloque = 0
            if dia == 0:
                horario[dias_semana[dia]][bloque].append([ramos, i+1])
            elif dia == 1:
                horario[dias_semana[dia]][bloque].append([ramos, i+1])
            elif dia == 2:
                horario[dias_semana[dia]][bloque].append([ramos, i+1])
            elif dia == 3:
                horario[dias_semana[dia]][bloque].append([ramos, i+1])
            elif dia == 4:
                horario[dias_semana[dia]][bloque].append([ramos, i+1])
            else:
                horario[dias_semana[dia]][bloque].append([ramos, i+1])
            dia = dia + 1
    return horario

def h4(datos,horario ):
    horario= {}
    return horario


def h5(datos):
    horario= {}
    return horario


def h6(datos):
    horario= {}
    return horario
