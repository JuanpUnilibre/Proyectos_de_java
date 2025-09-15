#Preludio--------------------------------------------------------------------------------------------
from colores import *
 
print("Hola, bienvenido al inventario de empanadas")
print("------------------------------------------------------")

#Parte de las gaseosas-------------------------------------------------------------------------------
nombre_vendedor = input("\n¿Cual es tu nombre? ")

if nombre_vendedor == "marian" or nombre_vendedor == "mariannel":
    print("\nBuenas noches bebeee 🥰, como estas? hermosa de seguro")
else:
    print(f"\nHola {nombre_vendedor}, espero que hayas tenido un buen dia de ventas")

print("\nComencemos de una vez con las gaseosas")

PRECIO_GASEOSA = 3000 #Precio promedio de las gaseosas

kola_roman_vendidas = int(input("\n¿Cuántas Kola Roman se vendieron hoy? "))
postobon_vendidas = int(input("\n¿Cuántas Postobon se vendieron hoy? "))
delvalle_vendidos = int(input("\n¿Cuántas Del Valle se vendieron hoy? "))
total_gaseosas_vendidas = ((kola_roman_vendidas + delvalle_vendidos + postobon_vendidas) * PRECIO_GASEOSA)
print(f"\n{VERDE}En gaseosas se vendieron: ${total_gaseosas_vendidas}  {RESET}")
print("------------------------------------------------------")

#Parte de los jugos naturales--------------------------------------------------------------------------
PRECIO_JUGO = 2500 #Precio promedio de los jugos naturales
print("\nAhora vamos con los jugos naturales")

jugos_vendidos = int(input("\n¿Cuántos jugos naturales se vendieron hoy? "))
total_jugos_vendidos = jugos_vendidos * PRECIO_JUGO
print(f"\nEn jugos naturales se vendieron: ${total_jugos_vendidos}")
if jugos_vendidos > 20:
    print(f" {VERDE} ¡Wow, se vendieron muchos jugos hoy! {RESET} ")
elif jugos_vendidos < 10:
    print(f" {ROJO} Podemos mejorar la venta de jugos. {RESET} ")
else:
    print("La venta de jugos estuvo bien.")
print("------------------------------------------------------")

#Parte de bebidas------------------------------------------------------------------------------------
total_precio_bebidas = total_gaseosas_vendidas + total_jugos_vendidos
print(f"\n{VERDE} En total, en bebidas (gaseosas mas jugos) se vendieron: ${total_precio_bebidas} mete esta plata en la Bolsa #1 que entregaremos al jefe {RESET} ")
print("------------------------------------------------------")

#Parte de los fritos---------------------------------------------------------------------------------
print("\n...Ahora vamos con fritos")
fritos_cocinados_hoy = int(input("\n¿Cuántos fritos se cocinaron hoy? "))
sobras_fritos_anoche = int(input("\n¿Cuántos fritos quedaron de anoche? "))

base = sobras_fritos_anoche + fritos_cocinados_hoy
print(f"\n{AMARILLO}La base de fritos de hoy en la mañana era de: {base} {RESET}")

sobras_fritos_hoy = int(input("\n¿Cuántos fritos sobraron hoy al final del dia? "))
fritos_vendidos_hoy = base - sobras_fritos_hoy
print(f"\nLos fritos vendidos hoy fueron: {fritos_vendidos_hoy}")

dinero_en_venta_fritos = fritos_vendidos_hoy * 2500

print(f"\nosea que en el dia de hoy en fritos nos hicimos: {dinero_en_venta_fritos}" )

PAGO_LA_FLACA = 40000 #Pago a la flaca por el dia (Cocinera)
PAGO_MIO = 40000 #Pago de mi parte por el dia (Vendedor/a)

dinero_nequi = int(input("\n¿Cuánto dinero se movió por Nequi hoy? "))

print("\nTuvimos gastos menores hoy? (si/no)")
if input().lower() == "si":
    print("\nCuanto gastamos?")
    gastos_menores = int(input())
else:
    gastos_menores = 0
dinero_fritos_enfisico = (dinero_en_venta_fritos - (PAGO_LA_FLACA + dinero_nequi + gastos_menores))
print(f"\nDeberias tener de dinero en fisico de fritos: {dinero_fritos_enfisico}, esto restando los pagos a la flaca, el dinero de nequi y los gastos menores")
print("------------------------------------------------------")

# Validación de caja-----------------------------------------------------------------------------------
respuesta = input("\n¿El dinero te dio exacto? (si/no) ").lower()
if respuesta == "si":
    print("\nBien, sigamos")
else:
    sobro_falto = input("\n¿Te sobro dinero (si/no)? ").lower()
    if sobro_falto == "no":
        print(f"\n{ROJO}Estas descuadrado{RESET}")
    elif sobro_falto == "si":
        supuesto = int(input("\n¿Cuánto dinero tienes en la mano? "))
        propina = supuesto - dinero_fritos_enfisico
        print(f"\n{VERDE}Te sobró de propina: {propina}, guarda eso para ti, y los ${dinero_fritos_enfisico} mételos en la bolsa #2 que le entregaremos al jefe  {RESET}")
        
print("\nMuy bien, ya casi terminamos")
dinero_global_enfisico = dinero_fritos_enfisico + total_precio_bebidas
print(f"\nLa suma global de dinero en fisico (fritos mas bebidas) que deberías tener: {dinero_global_enfisico}, eso por si lo querias saber, o comprobar, aunque ya a este punto los metiste en sus respectivas bolsas")
dinero_global_enfisicoEnd = dinero_fritos_enfisico + total_precio_bebidas - PAGO_MIO
print(f"\nY la suma global de dinero en fisico menos mi pago, que deberías tener: {dinero_global_enfisicoEnd}")
print("------------------------------------------------------")

#Cuentas finales------------------------------------------------------------------------------------
print(f"\nOkey, sumando la plata de Nequi, la plata en fisico de los fritos, y la plata de las bebidas, deberias tener en total: {dinero_nequi + dinero_fritos_enfisico + total_precio_bebidas}, este resultado es la ganancia del día de hoy de la empresa")

#Resumen del dia------------------------------------------------------------------------------------
if (nombre_vendedor == "marian" or nombre_vendedor == "mariannel"):
    print(f"{ROJO}Sueña rico linda<3{RESET}")
else:
    print(f"\nGracias por tu esfuerzo hoy {nombre_vendedor}, nos vemos mañana, que tengas buenas noches")




#################################################################################################
#################################################################################################
#Cuentas finales------------------------------------------------------------------------------------
# Guardar el reporte al finalizar el día

import os, sys
import datetime



def ruta_base():
    if getattr(sys, 'frozen', False):  
        # Si está empaquetado como .exe (PyInstaller)
        return os.path.dirname(sys.executable)
    else:
        # Si está corriendo como .py normal
        return os.path.dirname(os.path.abspath(__file__))

ganancia_total = dinero_nequi + dinero_fritos_enfisico + total_precio_bebidas

timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def guardar_reporte(nombre, total_gaseosas, total_jugos, dinero_fritos_enfisico, dinero_nequi, ganancia_total):
    ruta_archivo = os.path.join(ruta_base(), "reporte_dia.txt")

    with open(ruta_archivo, "a", encoding="utf-8") as archivo:
        archivo.write("=====================================\n")
        archivo.write(f"Vendedor: {nombre}\n")
        archivo.write(f"Fecha y hora: {timestamp}\n")
        archivo.write(f"Gaseosas vendidas: ${total_gaseosas}\n")
        archivo.write(f"Jugos vendidos: ${total_jugos}\n")
        archivo.write(f"Dinero físico fritos: ${dinero_fritos_enfisico}\n")
        archivo.write(f"Dinero en Nequi: ${dinero_nequi}\n")
        archivo.write(f"Ganancia total del día: ${ganancia_total}\n")
        archivo.write("=====================================\n\n")

    print("\n✅ El archivo se guardó en:", ruta_archivo)


guardar_reporte(
    nombre_vendedor,
    total_gaseosas_vendidas,
    total_jugos_vendidos,
    dinero_fritos_enfisico,
    dinero_nequi,
    ganancia_total
)

# Esperar antes de salir
input("Presiona Enter para salir...")
#################################################################################################