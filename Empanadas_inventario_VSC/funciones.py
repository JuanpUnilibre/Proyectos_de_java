from colores import *

def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print(f"{ROJO}⚠️ Por favor ingresa un número positivo.{RESET}")
                continue
            return valor
        except ValueError:
            print(f"{ROJO}⚠️ Entrada inválida. Debes ingresar un número entero.{RESET}")

