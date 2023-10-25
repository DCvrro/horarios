import random

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

def heuristica_aleatoria(datos):
    # Lista de horarios disponibles (bloques de 2 horas)
    horarios_disponibles = list(range(9, 18, 2))
    
    # Inicializar la asignación de horarios
    asignacion = {}

    # Obtener la lista de pruebas y barajarla aleatoriamente
    pruebas = list(datos.keys())
    random.shuffle(pruebas)

    for prueba in pruebas:
        if not horarios_disponibles:
            # Si no quedan horarios disponibles en el día, pasar al siguiente día
            horarios_disponibles = list(range(9, 18, 2))

        # Seleccionar un horario aleatorio de la lista de horarios disponibles
        horario = random.choice(horarios_disponibles)

        # Verificar si el horario seleccionado no excede las horas disponibles en un día (9 AM - 6 PM)
        if horario + 2 > 18:
            # Si excede, seleccionar un nuevo horario aleatorio
            horarios_disponibles.remove(horario)
            continue

        # Asignar la prueba al horario seleccionado
        asignacion[prueba] = horario
        
        # Actualizar la lista de horarios disponibles
        horarios_disponibles.remove(horario)

    return asignacion

# Heurística por Semestre
def heuristica_por_semestre(datos):
    # Lista de horarios disponibles (bloques de 2 horas)
    horarios_disponibles = list(range(9, 18, 2))
    
    # Inicializar la asignación de horarios
    asignacion = {}

    # Obtener la lista de pruebas y ordenarlas por semestre
    pruebas = list(datos.keys())
    pruebas.sort(key=lambda prueba: datos[prueba]['semestre'])

    for prueba in pruebas:
        # Obtener el semestre de la prueba actual
        semestre_actual = datos[prueba]['semestre']
        
        # Filtrar las pruebas que ya han sido asignadas en el mismo día para el semestre actual
        pruebas_semestre_actual = [p for p, h in asignacion.items() if datos[p]['semestre'] == semestre_actual and h[0] == horarios_disponibles[0]]
        
        if len(pruebas_semestre_actual) >= 4:
            # Si ya hay 4 pruebas del mismo semestre en el mismo día, pasar al siguiente día
            horarios_disponibles = list(range(9, 18, 2))
        
        # Seleccionar un horario aleatorio de la lista de horarios disponibles
        horario = horarios_disponibles[0]
        
        # Verificar si el horario seleccionado no excede las horas disponibles en un día (9 AM - 6 PM)
        if horario + 2 > 18:
            # Si excede, seleccionar un nuevo horario aleatorio
            horarios_disponibles.pop(0)
            if not horarios_disponibles:
                # Si no hay más horarios disponibles en el día, pasar al siguiente día
                horarios_disponibles = list(range(9, 18, 2))
            horario = horarios_disponibles[0]

        # Asignar la prueba al horario seleccionado
        asignacion[prueba] = (horario, horarios_disponibles[0])
        
        # Actualizar la lista de horarios disponibles
        horarios_disponibles.pop(0)
    
    return asignacion

# Heurística por Bloques Disponibles
def heuristica_por_bloques_disponibles(datos):
    pruebas = list(datos.keys())
    horarios_disponibles = [bloque for bloque in range(9, 18, 2)]  # Horarios disponibles de 9 AM a 6 PM
    random.shuffle(horarios_disponibles)  # Baraja la lista de horarios disponibles
    asignacion = {}
    for prueba in pruebas:
        if not horarios_disponibles:
            # Si no hay más horarios disponibles, vuelve a crear la lista
            horarios_disponibles = [bloque for bloque in range(9, 18, 2)]
            random.shuffle(horarios_disponibles)
        bloque_asignado = horarios_disponibles.pop(0)
        # Asignar la prueba al bloque disponible
        asignacion[prueba] = bloque_asignado
    return asignacion

# Heurística por Restricción de Día

def heuristica_por_restriccion_de_dia(datos):
    # Lista de horarios disponibles (bloques de 2 horas)
    horarios_disponibles = list(range(9, 18, 2))
    
    # Días laborables de la semana
    dias_laborables = list(range(5))
    
    # Inicializar la asignación de horarios
    asignacion = {}

    # Obtener la lista de pruebas
    pruebas = list(datos.keys())

    for prueba in pruebas:
        dia_asignado = None
        while dia_asignado is None:
            # Seleccionar un día aleatorio de la lista de días laborables
            dia = random.choice(dias_laborables)
            
            # Verificar si hay pruebas del mismo semestre en el mismo día
            pruebas_mismo_dia = [prueba for prueba, dia_asignado in asignacion.items() if datos[prueba]['semestre'] == datos[pruebas[0]]['semestre']]
            if not any(dia_asignado == dia for prueba, dia_asignado in asignacion.items()):
                dia_asignado = dia

        # Seleccionar un bloque horario disponible aleatorio
        horario = random.choice(horarios_disponibles)
        
        # Verificar si el bloque seleccionado no excede las horas disponibles en un día (9 AM - 6 PM)
        if horario + 2 > 18:
            # Si excede, seleccionar un nuevo bloque horario aleatorio
            horarios_disponibles.remove(horario)
            if not horarios_disponibles:
                # Si no hay más bloques horarios disponibles en el día, pasar al siguiente día
                horarios_disponibles = list(range(9, 18, 2))
            horario = random.choice(horarios_disponibles)

        # Asignar la prueba al día y bloque horario seleccionados
        asignacion[prueba] = (dia_asignado, horario)
        
        # Actualizar la lista de bloques horarios disponibles
        horarios_disponibles.remove(horario)
    
    return asignacion

# Heurística de Búsqueda Local
def heuristica_busqueda_local(datos):
    # Obtener la lista de pruebas y barajarla aleatoriamente
    pruebas = list(datos.keys())
    random.shuffle(pruebas)
    
    # Lista de horarios disponibles (bloques de 2 horas)
    horarios_disponibles = list(range(9, 18, 2))
    
    # Inicializar la asignación de horarios
    asignacion = {}
    
    # Asignar pruebas de manera aleatoria inicialmente
    for prueba in pruebas:
        horario = random.choice(horarios_disponibles)
        
        # Verificar si el horario seleccionado no excede las horas disponibles en un día (9 AM - 6 PM)
        if horario + 2 > 18:
            horarios_disponibles.remove(horario)
            if not horarios_disponibles:
                horarios_disponibles = list(range(9, 18, 2))
            horario = random.choice(horarios_disponibles)
        
        asignacion[prueba] = horario
        horarios_disponibles.remove(horario)

    # Función para evaluar la calidad de la asignación
def evaluar_asignacion(asignacion):
        # Implementa una métrica de calidad (puedes usar restricciones incumplidas, etc.)
        # ...

    # Evaluar la calidad de la asignación inicial
    mejor_asignacion = asignacion.copy()
    mejor_valor = evaluar_asignacion(asignacion)
    
    # Número máximo de iteraciones (puedes ajustarlo según tus necesidades)
    max_iteraciones = 1000
    
    for _ in range(max_iteraciones):
        # Seleccionar dos pruebas aleatorias para intercambiar
        prueba1, prueba2 = random.sample(pruebas, 2)
        
        # Realizar el intercambio de horarios entre las dos pruebas
        asignacion[prueba1], asignacion[prueba2] = asignacion[prueba2], asignacion[prueba1]
        
        # Evaluar la calidad de la nueva asignación
        valor_actual = evaluar_asignacion(asignacion)
        
        # Si la nueva asignación es mejor, aceptarla
        if valor_actual < mejor_valor:
            mejor_asignacion = asignacion.copy()
            mejor_valor = valor_actual
        else:
            # Si no es mejor, deshacer el intercambio
            asignacion[prueba1], asignacion[prueba2] = asignacion[prueba2], asignacion[prueba1]
    
    return mejor_asignacion

def obtener_semestre(asignatura, datos):
    for semestre, asignaturas in datos.items():
        if asignatura in asignaturas['asignaturas']:
            return semestre

def hay_tope_por_semestre(asignatura, dia, horario, datos):
    # Obten el semestre de la asignatura dada
    semestre_asignatura = obtener_semestre(asignatura, datos)

    # Recorre el horario para el día especificado
    for bloque in horario[dia]:
        asignaturas_bloque = horario[dia][bloque]

        # Si el bloque no está lleno y hay asignaturas
        if len(asignaturas_bloque) < 4 and asignaturas_bloque:
            # Verifica si alguna asignatura del mismo semestre ya está en el bloque
            for asignatura_en_bloque in asignaturas_bloque:
                semestre_en_bloque = obtener_semestre(asignatura_en_bloque, datos)
                if semestre_en_bloque == semestre_asignatura:
                    return True
    return False

def h_aleatoria(datos):
    dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']
    horario = {}
    for dia in dias:  #con esto asigno los dias de la semana de la libreta
        horario[dia] = {}
    bloques =  4
    asignaturas = []
    for sem in datos:
        for asig in datos[sem]['asignaturas']:
            asignaturas.append(asig)
    
    print(len(asignaturas))
    for dias in horario:
        #Creamos los bloques
        for i in range(bloques):
            horario[dias][i+1] = []
            

    validar = True 
    
    while validar:
        for day in horario:
            for block in horario[day]:
                if asignaturas != [] and len(horario[day][block]) < 4:
                    tmp = random.choice(asignaturas)
                    while hay_tope_por_semestre(tmp, day, horario, datos):
                        tmp = random.choice(asignaturas)
                    horario[day][block].append(tmp)
                    asignaturas.remove(tmp)
            if validar == False:
                break
        if asignaturas == []:
            validar = False
            break
        
    print(horario)
    
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
            
    while len(asignaturas) != 0:
        for day in horario:
            dia = []
            for bloque in horario[day]:
                validar = True
                while(validar):
                    if asignaturas != []:
                        tmp = random.choice(asignaturas)
                        semTmp = tmp.getSemestre()
                        if semTmp not in dia:
                            horario[day][bloque].append(tmp)
                            dia.append(semTmp) #A cada dia, le agrego los semestres que se evaluan
                            asignaturas.remove(tmp)
                    if len(horario[day][bloque]) == 4 or (asignaturas == []):
                        validar = False
                    break
    return horario


#reviso si existe una asignatura del mismo semestre en el mismo dia