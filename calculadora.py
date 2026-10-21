# calculadora.py

def sumar(cadena: str) -> int:
    # Si la cadena está vacía, devolvemos cero.
    if not cadena:
        return 0

    # Si contiene un número, lo convertimos a entero.
    return int(cadena)