import random

def juego_adivinanzas():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    print("¡Bienvenido al juego de adivinaza de números! \nHe seleccionado un número entre el 1 y el 100. ¿puedes adivinar cuál es?")

    while True:
        intento = int(input("Introduce tu número: "))
        intentos += 1

        if intento < numero_secreto:
            print("Muy bajo. Intentelo de nuevo")

        elif intento > numero_secreto:
            print("Muy alto. Intentelo de nuevo")

        else:
            print(f"¡Felizidades! Has acertado el número en {intentos} intentos.")
            break
        
if __name__ == "__main__":
    juego_adivinanzas()
                                                                                    



        
