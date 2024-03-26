# Escritura de Archivo de Texto:
# Crea un nuevo archivo llamado my_notes.txt.

archivo = "my_notes.txt"

#Abre el archivo my_notes.txt.
archivo_escritura = open(archivo, "w")

#Escribe al menos tres líneas de notas personales en el archivo.
archivo_escritura.write("line 1: Me llamo Angela. \n")
archivo_escritura.write("line 2: tengo 22 años. \n")
archivo_escritura.write("line 2: Soy de Ecuador. \n")
# cerramos el archivo de escritura
archivo_escritura.close()

# Abrimos el archivo my_notes.txt. de lectura
archivos = open(archivo, "r")

# Lee el contenido del archivo línea por línea utilizando el método adecuado.

print(archivos.readline())
print(archivos.readline())
print(archivos.readline())
# Cerramos el archivo después de leer
archivos.close()
