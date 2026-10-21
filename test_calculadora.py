# test_calculadora.py

from calculadora import sumar


def test_cadena_vacia_devuelve_cero():
    assert sumar("") == 0