#Parte de las gaseosas
PRECIO_GASEOSA = 3000

kola_roman_vendidas = int(input("\n¿Cuántas Kola Roman se vendieron hoy? "))
postobon_vendidas = int(input("\n¿Cuántas Postobon se vendieron hoy? "))
delvalle_vendidos = int(input("\n¿Cuántas Del Valle se vendieron hoy? "))
total_gaseosas_vendidas = ((kola_roman_vendidas + delvalle_vendidos + postobon_vendidas) * PRECIO_GASEOSA)
print(f"\nEn gaseosas se vendieron: ${total_gaseosas_vendidas} ")

#Parte de los jugos naturales
PRECIO_JUGO = 2500

jugos_vendidos = int(input("\n¿Cuántos jugos naturales se vendieron hoy? "))
total_jugos_vendidos = jugos_vendidos * PRECIO_JUGO
print(f"\nEn jugos naturales se vendieron: ${total_jugos_vendidos}")
if jugos_vendidos > 20:
    print("¡Wow, se vendieron muchos jugos hoy!")
else:
    print("Podemos mejorar la venta de jugos.")
    

#Parte de bebidas
total_precio_bebidas = total_gaseosas_vendidas + total_jugos_vendidos
print(f"\nEn total, en bebidas (gaseosas mas jugos) se vendieron: ${total_precio_bebidas} mete esta plata en la Bolsa #1 que entregaremos al jefe")


#Parte de los fritos
print("\n...Ahora vamos con fritos")
fritos_cocinados_hoy = int(input("\n¿Cuántos fritos se cocinaron hoy? "))
sobras_fritos_anoche = int(input("\n¿Cuántos fritos quedaron de anoche? "))

base = sobras_fritos_anoche + fritos_cocinados_hoy
print(f"\nLa base de fritos de hoy en la mañana era de: {base}")

sobras_fritos_hoy = int(input("\n¿Cuántos fritos sobraron hoy al final del dia? "))
fritos_vendidos_hoy = base - sobras_fritos_hoy
print(f"\nLos fritos vendidos hoy fueron: {fritos_vendidos_hoy}")

dinero_en_venta_fritos = fritos_vendidos_hoy * 2500

print(f"\nosea que en el dia de hoy en fritos nos hicimos: {dinero_en_venta_fritos}" )

PAGO_LA_FLACA = 40000
PAGO_MIO = 40000

dinero_nequi = int(input("\n¿Cuánto dinero se movió por Nequi hoy? "))

print("\nTuvimos gastos menores hoy? (si/no)")
if input().lower() == "si":
    print("\nCuanto gastamos?")
    gastos_menores = int(input())
else:
    gastos_menores = 0
dinero_fritos_enfisico = (dinero_en_venta_fritos - (PAGO_LA_FLACA + dinero_nequi + gastos_menores))
print(f"\nDeberias tener de dinero en fisico de fritos: {dinero_fritos_enfisico}, esto restando los pagos a la flaca, el dinero de nequi y los gastos menores")

# Validación de caja
respuesta = input("\n¿El dinero te dio exacto? (si/no) ").lower()
if respuesta == "si":
    print("\nBien, sigamos")
else:
    sobro_falto = input("\n¿Te sobro dinero (si/no)? ").lower()
    if sobro_falto == "no":
        print("\nEsta descuadrado")
    elif sobro_falto == "si":
        supuesto = int(input("\n¿Cuánto dinero tienes en la mano? "))
        propina = supuesto - dinero_fritos_enfisico
        print(f"\nTe sobró de propina: {propina}, guarda eso para ti, y los ${dinero_fritos_enfisico} mételos en la bolsa #2 que le entregaremos al jefe")
        
print("\nMuy bien, ya casi terminamos")
dinero_global_enfisico = dinero_fritos_enfisico + total_precio_bebidas
print(f"\nLa suma global de dinero en fisico (fritos mas bebidas) que deberías tener: {dinero_global_enfisico}, eso por si lo querias saber, o comprobar, aunque ya a este punto los metiste en sus respectivas bolsas")
dinero_global_enfisicoEnd = dinero_fritos_enfisico + total_precio_bebidas - PAGO_MIO
print(f"\nY la suma global de dinero en fisico menos mi pago, que deberías tener: {dinero_global_enfisicoEnd}")

#Cuentas finales

print(f"\nOkey, sumando la plata de Nequi, la plata en fisico de los fritos, y la plata de las bebidas, deberias tener en total: {dinero_nequi + dinero_fritos_enfisico + total_precio_bebidas}, este resultado es la ganancia del día de hoy de la empresa")

#Resumen del dia


print("\nGracias por tu esfuerzo el dia de hoy, nos vemos mañana")


        




