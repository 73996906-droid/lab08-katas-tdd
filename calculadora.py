# calculadora.py

def sumar(cadena: str) -> int:
    # Si la cadena está vacía, devolvemos cero.
    if not cadena:
        return 0

    # Separamos los números utilizando la coma.
    numeros = cadena.split(",")

    # Convertimos cada número a entero y los sumamos.
    return sum(int(n) for n in numeros)