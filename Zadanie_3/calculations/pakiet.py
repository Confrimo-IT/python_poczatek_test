import math

def wartosc_lokaty (wart_pocz, oprocent, okres):
    return (wart_pocz * (1 + oprocent/100) ** okres)

