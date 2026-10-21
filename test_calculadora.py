# test_calculadora.py

from calculadora import sumar


def test_cadena_vacia_devuelve_cero():
    assert sumar("") == 0

def test_un_solo_numero_devuelve_el_mismo_valor():
    assert sumar("5") == 5