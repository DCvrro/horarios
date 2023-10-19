import json
import random

# Lista de ramos simulados
cursos = [
    {"nombre": "Programación I", "secciones": [1, 2]},
    {"nombre": "Estructuras de Datos", "secciones": [1, 2]},
    {"nombre": "Redes de Computadoras", "secciones": [1, 2]},
    {"nombre": "Base de Datos", "secciones": [1, 2]},
    {"nombre": "Sistemas Operativos", "secciones": [1, 2]},
    # Agrega más ramos según sea necesario
]

# Generar datos simulados para las secciones
for curso in cursos:
    for seccion in curso["secciones"]:
        seccion_data = {
            "alumnos": random.randint(30, 40),
            "horarios": []
        }

        # Generar horarios simulados
        hora_inicio = 510  # 8:30 AM en minutos desde la medianoche
        while hora_inicio < 1140:  # Antes de las 7 PM
            seccion_data["horarios"].append({"hora_inicio": hora_inicio, "dias": random.sample(["L", "M", "X", "J", "V"], 3)})
            hora_inicio += 80  # Bloques de 80 minutos
            hora_inicio += 10  # Intervalo de 10 minutos

        curso[f"Sección {seccion}"] = seccion_data

# Guardar los datos en un archivo JSON
with open("base_de_datos.json", "w") as json_file:
    json.dump(cursos, json_file, indent=4)

print("Base de datos JSON creada con éxito.")






