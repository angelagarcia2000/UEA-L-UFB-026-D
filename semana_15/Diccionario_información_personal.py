# Crea un diccionario llamado informacion_personal que contenga información ficticia sobre una persona, incluyendo al menos las claves "nombre", "edad", "ciudad" y "profesion".

# Crear un Diccionario:

informacion_personal = {"nombre":"Angela",
                        "edad": 23 ,
                        "ciudad": "Lago Agrio",
                        "Carrera" :"Tecnologias de la informacion"}

# Acceder y Modificar Valores:

informacion_personal["ciudad"]= "Riobamba"
informacion_personal["profesión"] = "Contabilidad"

# Verificar Existencia de Claves:
print( "Teléfono" in informacion_personal)
informacion_personal ["Teléfono"] = "0968321754"

#Eliminar una Clave:
del (informacion_personal["edad"])

# Imprimir el Diccionario Final:
print(informacion_personal)