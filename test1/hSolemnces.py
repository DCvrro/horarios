import csv

# Definir la estructura de la malla curricular
malla = [
    ["Semestre 1", "Álgebra y Geometría", "Cálculo 1", "Química", "Programación", "Comunicación para la Ingeniería"],
    ["Semestre 2", "Álgebra Lineal", "Cálculo 2", "Mecánica", "Programación Avanzada", "CFG"],
    ["Semestre 3", "EDO", "Cálculo 3", "Calor y Ondas", "Estructura de Datos y Algoritmos", "Redes de Datos"],
    ["Semestre 4", "Probabilidad y Estadísticas", "Electrónica y Electrotecnia", "Electricidad y Magnetismo", "Bases de Datos", "Desarrollo Web y Móvil"],
    ["Semestre 5", "Optimización", "Taller de Redes y Servicios", "Proyecto en TICs 1", "Bases de Datos Avanzadas", "CFG"],
    ["Semestre 6", "Contabilidad y Costos", "Arquitectura y Organización de Computadores", "Señales y Sistemas", "Sistemas Operativos", "CFG"],
    ["Semestre 7", "Gestión Organizacional", "Sistemas Distribuidos", "Comunicaciones Digitales", "Ingeniería de Software", "CFG"],
    ["Semestre 8", "Introducción a la Economía", "Tecnologías Inalámbricas", "Criptografía y Seguridad en Redes", "IA", "Evaluación de Proyectos TIC"],
    ["Semestre 9", "Electivo Profesional", "Arquitecturas Emergentes", "Electivo Profesional", "Arquitectura de Software", "Data Science"],
    ["Semestre 10", "Electivo Profesional", "Electivo Profesional", "Electivo Profesional", "Electivo Profesional", "Proyecto en TICS 2"]
]

# Nombre del archivo CSV de salida
nombre_archivo = "malla_curricular.csv"

# Escribir la información en el archivo CSV
with open(nombre_archivo, mode='w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    
    # Escribir el encabezado
    escritor_csv.writerow(["Semestre", "Asignatura 1", "Asignatura 2", "Asignatura 3", "Asignatura 4", "Asignatura 5"])
    
    # Escribir los datos de la malla
    for fila in malla:
        escritor_csv.writerow(fila)
        
print(f"La malla curricular se ha guardado en {nombre_archivo}")
