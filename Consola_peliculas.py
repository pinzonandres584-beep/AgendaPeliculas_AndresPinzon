#consola_peliculas.py
"""
Agenda de peliculas.
Modulo de interacci0n por consola.
"""
import modulo_peliculas as mod

def mostrar_informacion_pelicula(pelicula: dict)-> None:
    """Imprime los detalles de la pelicula"""       
    nombre = pelicula["nombre"]
    genero = pelicula["genero"]
    duracion = pelicula["duracion"]
    anio = pelicula["anio"]
    clasificacion = pelicula["clasificacion"]
    hora = pelicula["hora"]
    dia = pelicula["dia"]
    
    print("Nombre: " + nombre + " - Anio: " + str(anio) + " - Duracion: " + str(duracion) + "  mins" )
    print("Genero: " + genero + " - Clasificacion: " + clasificacion)
    
    if (hora//100 < 10):
        hora_formato = "0"+ str(hora//100)
    else:
        hora_formato = str(hora//100)
    
    if (hora%100 < 10):
        min_formato = "0"+ str(hora%100)
    else:
        min_formato = str(hora%100)

    print("Dia: " + dia + " Hora: " + hora_formato + ":" + min_formato)

def ejecutar_encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->None:
    # Llamamos a la función del módulo para obtener el diccionario de la más larga
    mas_larga = mod.encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5)
    print("La película con mayor duración es:")
    mostrar_informacion_pelicula(mas_larga)

def ejecutar_consultar_duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->None:
    # Obtenemos el promedio formateado en HH:MM
    promedio = mod.duracion_promedio_peliculas(p1, p2, p3, p4, p5)
    print("La duración promedio de las películas en la agenda es: " + promedio)

def ejecutar_encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->None:
    # Pedimos al usuario el año de referencia
    anio_limite = int(input("Ingrese el año para consultar estrenos: "))
    estrenos = mod.encontrar_estrenos(p1, p2, p3, p4, p5, anio_limite)
    print("Películas estrenadas después de " + str(anio_limite) + ": " + estrenos)

def ejecutar_cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->None:
    # Contamos las películas con esa clasificación
    cantidad = mod.cuantas_peliculas_18_mas(p1, p2, p3, p4, p5)
    print("En la agenda hay " + str(cantidad) + " película(s) con clasificación 18+.")
    
def ejecutar_reagendar_pelicula(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->None:
    print("Reagendar una pelicula de la agenda")
    nombre = input("Ingrese el nombre de la pelicula que desea reagendar: ")
    pelicula = mod.encontrar_pelicula(nombre,p1,p2,p3,p4,p5)
    
    if pelicula is None:
        print("No hay ninguna pelicula con este nombre")
    else:
        # Pedimos los datos necesarios para reagendar
        nueva_hora = int(input("Ingrese la nueva hora (formato 24h, ej: 1530): "))
        nuevo_dia = input("Ingrese el nuevo día de la semana: ")
        opcion_control = input("¿Desea aplicar control horario? (si/no): ").lower()
        control_bool = True if opcion_control == "si" else False
        
        # Llamamos a la lógica de reagendamiento
        exito = mod.reagendar_pelicula(pelicula, nueva_hora, nuevo_dia, control_bool, p1, p2, p3, p4, p5)
        
        if exito:
            print("¡La película ha sido reagendada exitosamente!")
        else:
            print("No se pudo reagendar. Verifique conflictos de horario o restricciones del sistema.")

def ejecutar_decidir_invitar(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->None:
    print("Decidir si se puede invitar a alguien a ver una pelicula")
    nom_peli = input("Ingrese el nombre de la pelicula: ")
    pelicula = mod.encontrar_pelicula(nom_peli,p1,p2,p3,p4,p5)

    if pelicula is None:
        print("No hay ninguna pelicula con este nombre")
    else:
        # Pedimos datos del invitado
        edad = int(input("Ingrese la edad del invitado: "))
        autorizacion_txt = input("¿El invitado tiene autorización de sus padres? (si/no): ").lower()
        tiene_autorizacion = True if autorizacion_txt == "si" else False
        
        # Llamamos a la lógica de invitación
        puede_invitar = mod.decidir_invitar(pelicula, edad, tiene_autorizacion)
        
        if puede_invitar:
            print("¡Sí! Puedes invitar a esta persona a ver " + pelicula["nombre"])
        else:
            print("Lo sentimos, esta persona no cumple los requisitos para ver " + pelicula["nombre"])
  
def iniciar_aplicacion():
    # Creamos las películas con los nombres que solicitaste
    pelicula1 = mod.crear_pelicula("John Wick", "Acción, Suspenso", 101, 2014, '18+', 2100, "Viernes")
    pelicula2 = mod.crear_pelicula("Misión Imposible", "Acción, Aventura", 110, 1996, '13+', 1500, "Sábado")  
    pelicula3 = mod.crear_pelicula("Shrek", "Familiar, Comedia", 90, 2001, 'Todos', 1000, "Domingo")
    pelicula4 = mod.crear_pelicula("Coraline", "Animación, Terror", 100, 2009, '7+', 1800, "Lunes")
    pelicula5 = mod.crear_pelicula("El Castillo Ambulante", "Animación, Fantasía", 119, 2004, 'Todos', 1400, "Miércoles")   
    
    ejecutando = True
    while ejecutando:            
        print("\n\nMi agenda de peliculas" +"\n"+("-"*50))
        # Se muestran los datos iniciales de las 5 películas
        for i, p in enumerate([pelicula1, pelicula2, pelicula3, pelicula4, pelicula5], 1):
            print("Pelicula " + str(i))
            mostrar_informacion_pelicula(p)
            print("-"*50)
        
        ejecutando = mostrar_menu_aplicacion(pelicula1, pelicula2, pelicula3, pelicula4, pelicula5)

        if ejecutando:
            input("Presione cualquier tecla para continuar ... ")

def mostrar_menu_aplicacion(p1: dict, p2: dict, p3: dict, p4:dict, p5:dict) -> bool:
    print("Menu de opciones")
    print(" 1 - Consultar pelicula mas larga")
    print(" 2 - Consultar duracion promedio de las peliculas")
    print(" 3 - Consultar peliculas de estreno")
    print(" 4 - Consultar cuantas peliculas tienen clasificacion 18+")
    print(" 5 - Reagendar pelicula")
    print(" 6 - Verificar si se puede invitar a alguien")    
    print(" 7 - Salir de la aplicacion")

    opcion_elegida = input("Ingrese la opcion que desea ejecutar: ").strip()
    
    continuar_ejecutando = True

    if opcion_elegida == "1":
        ejecutar_encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5)
    elif opcion_elegida == "2":
        ejecutar_consultar_duracion_promedio_peliculas(p1, p2, p3, p4, p5)
    elif opcion_elegida == "3":
        ejecutar_encontrar_estrenos(p1, p2, p3, p4, p5)
    elif opcion_elegida == "4":
        ejecutar_cuantas_peliculas_18_mas(p1, p2, p3, p4, p5)        
    elif opcion_elegida == "5":
        ejecutar_reagendar_pelicula(p1, p2, p3, p4, p5) 
    elif opcion_elegida == "6":
        ejecutar_decidir_invitar(p1, p2, p3, p4, p5) 
    elif opcion_elegida == "7":
        continuar_ejecutando = False
    else:
        print("La opcion " + opcion_elegida + " no es una opcion valida.")
    
    return continuar_ejecutando

    iniciar_aplicacion()