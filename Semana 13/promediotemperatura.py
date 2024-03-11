#calcular el promedio de de temperatura de una ciudad

temperaturas = [
    [   # Ciudad Tena
        [   # Semana 1
            {"dia": "Lunes", "temp": 32},
            {"dia": "Martes", "temp": 55},
            {"dia": "Miércoles", "temp": 78},
            {"dia": "Jueves", "temp": 77},
            {"dia": "Viernes", "temp": 78},
            {"dia": "Sábado", "temp": 74},
            {"dia": "Domingo", "temp": 73}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temp": 34},
            {"dia": "Martes", "temp": 25},
            {"dia": "Miércoles", "temp": 24},
            {"dia": "Jueves", "temp": 57},
            {"dia": "Viernes", "temp": 84},
            {"dia": "Sábado", "temp": 24},
            {"dia": "Domingo", "temp": 16}
        ],
        [  # Semana 3
            {"dia": "Lunes", "temp": 74},
            {"dia": "Martes", "temp": 41},
            {"dia": "Miércoles", "temp": 45},
            {"dia": "Jueves", "temp": 84},
            {"dia": "Viernes", "temp": 48},
            {"dia": "Sábado", "temp": 94},
            {"dia": "Domingo", "temp": 45}
        ],
        [  # Semana 4
            {"dia": "Lunes", "temp": 25},
            {"dia": "Martes", "temp": 28},
            {"dia": "Miércoles", "temp": 82},
            {"dia": "Jueves", "temp": 72},
            {"dia": "Viernes", "temp": 24},
            {"dia": "Sábado", "temp": 82},
            {"dia": "Domingo", "temp": 21}
        ]]]


# Calcular el promedio de temperaturas para cada ciudad y semana


for ciudad in temperaturas:
    for semana in ciudad:
        suma = 0
        for dia in semana:
            suma += dia['temp']
        print(suma,)