"""Este programa realiza el método de cifrada de Diffie-Hellman."""
import os


def procesamiento(p, g, x):
    """Retorna el valor de la operación de Diffie-Hellman."""
    y = (g**x) % p
    return y


if __name__ == "__main__":
    os.system("cls")

    p = int(input("Ingrese el número primo público"
                  " para el método de encriptación: "))

    g = int(input("Ingrese un número a cifrar: "))

    # Solicitamos la clave privada de los usuarios
    a = int(input("Ingrese la clave privada que usará el usuario 1: "))
    b = int(input("Ingrese la clave privada que usará el usuario 2: "))

    # Obtenemos las claves públicas que obtendrían los dos usuarios
    A = procesamiento(p, g, a)
    B = procesamiento(p, g, b)

    # Obtenemos el mensaje cifrado
    K1 = procesamiento(p, B, a)
    K2 = procesamiento(p, A, b)

    if K1 == K2:
        print(f"La clave privada compartida es: {K1}")
    else:
        print("Error en el cifrado")
