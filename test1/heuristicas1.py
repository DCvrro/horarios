import csv
import random

# Leer el archivo CSV
def leer_malla_curricular(archivo_csv):
    malla = {}
    with open(archivo_csv, 'r', encoding='iso-8859-1') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            semestre = row['Semestre']
            asignaturas = [row[f'Asignatura {i}'] for i in range(1, 6)]
            malla[semestre] = asignaturas
    return malla

# Heurística 1: Asignación aleatoria de horarios
def heuristica_aleatoria(malla):
    horarios = {}
    for semestre, asignaturas in malla.items():
        for asignatura in asignaturas:
            horarios[asignatura] = (semestre, random.choice(["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]), random.choice(["9:00 AM", "2:00 PM"]))
    return horarios

# Heurística 2: Asignación en orden
def heuristica_orden(malla):
    horarios = {}
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    horas = ["9:00 AM", "2:00 PM"]
    for semestre, asignaturas in malla.items():
        for dia in dias:
            for hora in horas:
                for asignatura in asignaturas:
                    horarios[asignatura] = (semestre, dia, hora)
    return horarios

# Heurística 3: Asignación equitativa de pruebas por día
def heuristica_equitativa(malla):
    horarios = {}
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    horas = ["9:00 AM", "2:00 PM"]
    for semestre, asignaturas in malla.items():
        for dia in dias:
            for hora in horas:
                for asignatura in asignaturas:
                    horarios[asignatura] = (semestre, dia, hora)
    return horarios

# Nombre del archivo CSV
archivo_csv = "malla_curricular.csv"

# Leer la malla curricular desde el archivo CSV
malla_curricular = leer_malla_curricular(archivo_csv)

# Aplicar las heurísticas a la malla curricular
horarios_aleatorios = heuristica_aleatoria(malla_curricular)
horarios_ordenados = heuristica_orden(malla_curricular)
horarios_equitativos = heuristica_equitativa(malla_curricular)

# Mostrar los horarios generados por cada heurística
print("Horarios generados por heurística aleatoria:")
for asignatura, horario in horarios_aleatorios.items():
    print(f"{asignatura}: Semestre {horario[0]}, Día {horario[1]}, Hora {horario[2]}")

print("\nHorarios generados por heurística en orden:")
for asignatura, horario in horarios_ordenados.items():
    print(f"{asignatura}: Semestre {horario[0]}, Día {horario[1]}, Hora {horario[2]}")

print("\nHorarios generados por heurística equitativa:")
for asignatura, horario in horarios_equitativos.items():
    print(f"{asignatura}: Semestre {horario[0]}, Día {horario[1]}, Hora {horario[2]}")
