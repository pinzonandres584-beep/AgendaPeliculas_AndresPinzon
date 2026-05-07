#Modulo_peliculas.2
"""
Agenda de peliculas.
Módulo de cálculos.
"""

def crear_pelicula(nombre: str, genero: str, duracion: int, anio: int, 
                  clasificacion: str, hora: int, dia: str) -> dict:
    # Construimos el diccionario con las llaves que nos piden
    pelicula = {
        "nombre": nombre,
        "genero": genero,
        "duracion": duracion,
        "anio": anio,
        "clasificacion": clasificacion,
        "hora": hora,
        "dia": dia
    }
    return pelicula[cite: 1]

def encontrar_pelicula(nombre_pelicula: str, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> dict:
    # Revisamos cada película para ver si el nombre coincide
    if p1["nombre"] == nombre_pelicula: return p1
    if p2["nombre"] == nombre_pelicula: return p2
    if p3["nombre"] == nombre_pelicula: return p3
    if p4["nombre"] == nombre_pelicula: return p4
    if p5["nombre"] == nombre_pelicula: return p5
    return None[cite: 1]

def encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> dict:
    # Comparamos las duraciones una por una
    mas_larga = p1
    if p2["duracion"] > mas_larga["duracion"]: mas_larga = p2
    if p3["duracion"] > mas_larga["duracion"]: mas_larga = p3
    if p4["duracion"] > mas_larga["duracion"]: mas_larga = p4
    if p5["duracion"] > mas_larga["duracion"]: mas_larga = p5
    return mas_larga[cite: 1]

def duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> str:
    # Sumamos y dividimos por 5
    total = p1["duracion"] + p2["duracion"] + p3["duracion"] + p4["duracion"] + p5["duracion"]
    promedio = total // 5
    horas = promedio // 60
    minutos = promedio % 60
    # Retornamos en formato HH:MM
    return str(horas).zfill(2) + ":" + str(minutos).zfill(2)[cite: 1]

def encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, anio: int) -> str:
    estrenos = []
    if p1["anio"] > anio: estrenos.append(p1["nombre"])
    if p2["anio"] > anio: estrenos.append(p2["nombre"])
    if p3["anio"] > anio: estrenos.append(p3["nombre"])
    if p4["anio"] > anio: estrenos.append(p4["nombre"])
    if p5["anio"] > anio: estrenos.append(p5["nombre"])
    
    if not estrenos:
        return "Ninguna"
    return ", ".join(estrenos)[cite: 1]

def cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> int:
    contador = 0
    if p1["clasificacion"] == "18+": contador += 1
    if p2["clasificacion"] == "18+": contador += 1
    if p3["clasificacion"] == "18+": contador += 1
    if p4["clasificacion"] == "18+": contador += 1
    if p5["clasificacion"] == "18+": contador += 1
    return contador[cite: 1]

def reagendar_pelicula(peli:dict, nueva_hora: int, nuevo_dia: str, 
                       control_horario: bool, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->bool:
    # 1. 
                         Conflicto de horario: que no haya otra película a la misma hora y día
    for p in [p1, p2, p3, p4, p5]:
        if p != peli and p["dia"] == nuevo_dia and p["hora"] == nueva_hora:
            return False[cite: 1]
    
    # 2. Reglas de control horario
    if control_horario:
        genero = peli["genero"].lower()
        # Documentales tarde
        if "documental" in genero and nueva_hora >= 2200: return False
        # Dramas viernes
        if "drama" in genero and nuevo_dia.lower() == "viernes": return False
        # Entre semana muy tarde o muy temprano
        dias_semana = ["lunes", "martes", "miércoles", "miercoles", "jueves", "viernes"]
        if nuevo_dia.lower() in dias_semana:
            if nueva_hora >= 2300 or nueva_hora < 600: return False[cite: 1]
            
    peli["hora"] = nueva_hora
    peli["dia"] = nuevo_dia
    return True[cite: 1]

def decidir_invitar(peli: dict, edad_invitado: int, autorizacion_padres: bool)->bool:
    if edad_invitado >= 18: return True
    
    genero = peli["genero"].lower()
    # Restricciones de edad por género
    if edad_invitado < 15 and "terror" in genero: return False
    if edad_invitado <= 10 and "familiar" not in genero: return False
    
    # Clasificación vs Edad
    clas = peli["clasificacion"]
    necesita_permiso = False
    if clas == "18+" and edad_invitado < 18: necesita_permiso = True
    elif clas == "16+" and edad_invitado < 16: necesita_permiso = True
    elif clas == "13+" and edad_invitado < 13: necesita_permiso = True
    elif clas == "7+" and edad_invitado < 7: necesita_permiso = True
    
    if necesita_permiso and "documental" not in genero:
        return autorizacion_padres
    return True[cite: 1]
