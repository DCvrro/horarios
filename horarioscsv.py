import random
import csv

# Información base
aulas_edificio1 = [f"1{str(sala).zfill(2)}" for sala in range(1, 6)]
aulas_edificio2 = [f"3{str(sala).zfill(2)}" for sala in range(11, 16)]
horarios = [
    "Lunes 8:30 AM - 9:50 AM",
    "Lunes 10:00 AM - 11:20 AM",
    "Martes 8:30 AM - 9:50 AM",
    "Martes 10:00 AM - 11:20 AM",
    "Miércoles 8:30 AM - 9:50 AM",
    "Miércoles 10:00 AM - 11:20 AM",
    "Jueves 8:30 AM - 9:50 AM",
    "Jueves 10:00 AM - 11:20 AM",
    "Viernes 8:30 AM - 9:50 AM",
    "Viernes 10:00 AM - 11:20 AM"
]
horario_miercoles_libre = "Miércoles 11:30 AM - 12:50 PM"

# Crear 20 ramos de informática aleatorios
ramos_informatica = random.sample(range(1, 21), 20)
cursos = [f"Informatica{ramo}" for ramo in ramos_informatica]

# Generar secciones aleatorias para cada curso
datos_secciones = []
for curso in cursos:
    num_secciones = random.randint(2, 4)
    for _ in range(num_secciones):
        aula = random.choice(aulas_edificio1 if random.random() < 0.5 else aulas_edificio2)
        horario_catedra = random.sample(horarios, 2)
        horario_ayudantia = random.choice(horarios)
        
        # Aplicar restricción de horario del miércoles
        if "Miércoles" in horario_catedra or "Miércoles" in horario_ayudantia:
            horario_catedra = [horario_miercoles_libre]
            horario_ayudantia = horario_miercoles_libre

        seccion = {
            "Curso": curso,
            "Aula": aula,
            "Horario Catedra": ', '.join(horario_catedra),
            "Horario Ayudantia": horario_ayudantia
        }
        datos_secciones.append(seccion)

# Guardar la información en un archivo CSV
with open("horario_informatica.csv", "w", newline="") as csvfile:
    fieldnames = ["Curso", "Aula", "Horario Catedra", "Horario Ayudantia"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for seccion in datos_secciones:
        writer.writerow(seccion)

print("Archivo CSV 'horario_informatica.csv' creado exitosamente.")
