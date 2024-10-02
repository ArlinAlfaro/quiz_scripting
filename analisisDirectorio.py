import os
import sys

def analizar_archivos(texto, palabra):# Funcion para contar las palabras
    return texto.lower().split().count(palabra.lower())

def analizar_informe(ruta_archivo): #Función que analiza los datos
    try:
        with open(ruta_archivo, 'r') as archivo:
            lineas = archivo.readlines()
            cantidad_lineas = len(lineas)
            cantidad_palabras = sum(len(linea.split()) for linea in lineas)
            contenido = ' '.join(lineas)
            cantidad_python = analizar_archivos(contenido, 'Python')
        return cantidad_lineas, cantidad_palabras, cantidad_python
    except FileNotFoundError:
        print("Error: El archivo no existe.")
        return None
    except PermissionError:
        print("Error: No se puede leer el archivo.")
        return None

def generar_informe(directorio, archivos_info):#Función que genera el informe
    informe_ruta = os.path.join(directorio, 'informe.txt')
    with open(informe_ruta, 'w') as informe:
        if archivos_info:
            for archivo, info in archivos_info.items():
                informe.write(
    f"""Nombre del archivo: {archivo}
Numero de lineas: {info['lineas']}
Numero total de palabras: {info['palabras']}
Numero de veces que aparece 'Python': {info['python']}

"""
)
        else:
            informe.write("No se encontraron archivos de texto.\n")

def main(): #Funciión principal para ejecutarlo, con verificaciones
    if len(sys.argv) != 2:
        print("Modo de uso: python script.py <directorio>")
        sys.exit(1)

    directorio = sys.argv[1]

    if not os.path.isdir(directorio):
        print("Error: El directorio no existe.")
        sys.exit(1)

    archivos_info = {}
    
    try:
        for archivo in os.listdir(directorio):
            if archivo.endswith('.txt'):
                ruta_archivo = os.path.join(directorio, archivo)
                info = analizar_informe(ruta_archivo)
                if info:
                    archivos_info[archivo] = {
                        'lineas': info[0],
                        'palabras': info[1],
                        'python': info[2]
                    }
    except OSError as e:
        print(f"Error al acceder al directorio: {e}")
        sys.exit(1)

    generar_informe(directorio, archivos_info)

if __name__ == "__main__":
    main()
