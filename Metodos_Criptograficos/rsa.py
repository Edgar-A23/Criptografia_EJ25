"""Método de encriptación RSA."""

import random


def coprimo_validacion(i, z):
    """Se comprueba si el valor dado i es un coprimio de z."""
    while z:
        i, z = z, i % z
    # Si el máximo común divisor es 1, entonces son coprimos
    if i == 1:
        return True
    if i != 1:
        return False


def encriptación(p, q, msg, rango):
    """Se realiza el proceso de encriptación y desencriptación del mensaje."""
    n = p * q
    z = (p - 1) * (q - 1)

    # k debe ser un entero entre 1 y z
    # K deber ser coprimo de z (unico factor común = 1)
    # Buscamos los valores posibles para k
    k_posibles = []
    for i in range(z):
        if coprimo_validacion(i, z):
            k_posibles.append(i)

    # Elegimos un valor aleatorio de la lista de K
    k = random.choice(k_posibles)

    # Buscamos los valores posibles para j
    j_posibles = []
    for i in range(rango):
        j = (1 + i * z) / k
        if j.is_integer():
            j_posibles.append(j)

    # Elegimos un valor aleatorio de la lista de J
    j = random.choice(j_posibles)

    # Encriptamos el mensaje
    cifrado = (msg**k) % n
    print(f"El mensaje cifrado es: {cifrado}\n")

    # Desencriptamos el mensaje
    desencriptado = (cifrado**j) % n

    """
    Comprobamos si el mensaje desencriptado concuerda con el mensaje original
    Este proceso comprueba la confidencialidad del mensaje enviado
    Solo el receptor puede recuperar el mensaje original con su clave privada
    """
    if msg == desencriptado:
        print(
            "El proceso de encriptación funciona adecuadamente,"
            " el mensaje mantiene la confidencialidad"
        )

    """
    Comprobamos si el mensaje desencriptado concuerda con el mensaje original
    tras encriptar usando la clave privada
    Este proceso comprueba la integridad y autenticidad del mensaje enviado
    Solo el dueño de la clave privada puede encriptar el mensaje original
    De otra manera la información recibida no coincidiría con la original
    """
    encriptación = (msg**j) % n
    desencriptado = (encriptación**k) % n
    if msg == desencriptado:
        print(
            "El mensaje esta integro,"
            " coincide con el mensaje original esperado"
            )
    else:
        print(
            "El mensaje fue comprometido en el envío,"
            " no coincide con el mensaje original esperado"
        )


while __name__ == "__main__":
    print("Ingresamos los valores para la clave pública\n")
    p = int(input("Ingrese un número primo 'p' cualquiera: \n"))
    q = int(input("Ingrese otro número primo 'q' cualquiera"
                  " distinto al 'p': \n"))
    while p <= 1:
        print("El número primo debe ser mayor a 0")
        p = int(input("Ingrese un número 'p' primo cualquiera: \n"))
    while q <= 1:
        print("El número primo debe ser mayor a 0")
        q = int(
            input("Ingrese otro número 'q' primo cualquiera"
                  " distinto al primero: \n")
        )
    # Ingresamos los parametros a usar para el método
    msg = input("Ingrese el mensaje a cifrar: \n")

    # Delimitamos un rango de valores para obtener la clave privada j
    rango = 1000
    encriptación(p, q, msg, rango)
    # Preguntamos si desea realizar otra encriptación
    while True:
        opcion = int(
                    input(
                        "¿Desea realizar otra encriptación con otro mensaje?"
                        " (Si: 1/ No: Cualquier otro numero)\n"
                    )
                )
        if opcion != 1:
            break
        else:
            msg = input("Ingrese el mensaje a cifrar: \n")
            encriptación(p, q, msg, rango)
            continue
