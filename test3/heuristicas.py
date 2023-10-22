import random

# Definir los datos de entrada
# ...

# Heurística Aleatoria
def heuristica_aleatoria(datos):
    # Lista de horarios disponibles (bloques de 2 horas)
    horarios_disponibles = list(range(9, 18, 2))
    
    # Inicializar la asignación de horarios
    asignacion = {}

    # Obtener la lista de pruebas y barajarla aleatoriamente
    pruebas = list(datos.keys())
    random.shuffle(pruebas)

    for prueba in pruebas:
        # Seleccionar un horario aleatorio de la lista de horarios disponibles
        horario = random.choice(horarios_disponibles)
        
        # Verificar si el horario seleccionado no excede las horas disponibles en un día (9 AM - 6 PM)
        if horario + 2 > 18:
            # Si excede, seleccionar un nuevo horario aleatorio
            horarios_disponibles.remove(horario)
            if not horarios_disponibles:
                # Si no hay más horarios disponibles en el día, pasar al siguiente día
                horarios_disponibles = list(range(9, 18, 2))
            horario = random.choice(horarios_disponibles)

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
        asignacion[prueba] = horario
        
        # Actualizar la lista de horarios disponibles
        horarios_disponibles.pop(0)
    
    return asignacion

# Heurística por Bloques Disponibles
def heuristica_por_bloques_disponibles(datos):
    # Lista de horarios disponibles (bloques de 2 horas)
    horarios_disponibles = list(range(9, 18, 2))
    
    # Inicializar la asignación de horarios
    asignacion = {}

    # Obtener la lista de pruebas
    pruebas = list(datos.keys())

    for prueba in pruebas:
        # Seleccionar un bloque horario disponible aleatorio
        bloque_asignado = random.choice(horarios_disponibles)
        
        # Verificar si el bloque seleccionado no excede las horas disponibles en un día (9 AM - 6 PM)
        if bloque_asignado + 2 > 18:
            # Si excede, seleccionar un nuevo bloque horario aleatorio
            horarios_disponibles.remove(bloque_asignado)
            if not horarios_disponibles:
                # Si no hay más bloques horarios disponibles en el día, pasar al siguiente día
                horarios_disponibles = list(range(9, 18, 2))
            bloque_asignado = random.choice(horarios_disponibles)

        # Asignar la prueba al bloque horario seleccionado
        asignacion[prueba] = bloque_asignado
        
        # Actualizar la lista de bloques horarios disponibles
        horarios_disponibles.remove(bloque_asignado)
    
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
