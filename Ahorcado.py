import os   #El os es una libreria que nos sirve para interactuar con el sistema operativo

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')   #El cls es para limpiar y el nt es la extención que se va a utilizar

def ingresa_palabra():
    limpiar_pantalla()
    palabra = input("Introduce la palabra a adivinar: ").lower()
    limpiar_pantalla()
    return palabra

def mostrar_palabra_secreta(palabra, letras_adivinadas):
    palabra_secreta = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            palabra_secreta += letra
        else:
            palabra_secreta += "_"
    return palabra_secreta

def ahorcado(intentos):
    dibujos_ahorcado = [
        """
                       ___
                      |   |
                          |
                          |
                          |
                    ______|
        """,
        """
                       ___
                      |   |
                      O   |
                          |
                          |
                    ______|
        """,
        """
                       ___
                      |   |
                     _O   |
                          |
                          |
                    ______|
        """,
        """
                       ___
                      |   |
                     _O/  |
                          |
                          |
                    ______|
        """,
        """
                       ___
                      |   |
                     _O/  |
                      |   |
                          |
                    ______|
        """,
        """
                       ___
                      |   |
                     _O/  |
                      |   |
                       \  |
                    ______|
        """,
        """
                       ___
                      |   |
                     _O/  |
                      |   |
                     / \  |
                    ______|
        """
    ]
    print(dibujos_ahorcado[intentos])

def jugar(palabra):
    letras_adivinadas = set()
    intentos_maximos = 7
    intentos = 0

    while intentos < intentos_maximos:
        palabra_secreta = mostrar_palabra_secreta(palabra, letras_adivinadas)
        print(f"Palabra: {palabra_secreta}")
        ahorcado(intentos)
        letra = input("Introduce una letra: ").lower()

         abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        if letra in abecedario:
            print("Tu letra esta dentro.")

        else:
            print("No se permiten numeros.")
        
        if letra not in palabra:
            intentos += 1
            print(f"Letra incorrecta. Te quedan {intentos_maximos - intentos} intentos.")
        else:
            print("Adivinaste una letra.")
            
        if letra in letras_adivinadas:
            print("ya has intentado con esta letra ocupa otro")
            continue
        letras_adivinadas.add(letra)
        
        if set(palabra) == letras_adivinadas:
            print("Has adivinado la palabra.")
            break

    if intentos == intentos_maximos:
        print(f"Perdiste. La palabra es: {palabra}")

palabra_a_adivinar = ingresa_palabra()
jugar(palabra_a_adivinar)
