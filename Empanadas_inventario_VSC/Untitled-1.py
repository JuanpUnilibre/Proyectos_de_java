fritos_cocinados_hoy = int(input("¿Cuántos fritos se cocinaron hoy? "))
sobras_fritos_anoche = int(input("¿Cuántos fritos quedaron de anoche? "))

base = sobras_fritos_anoche + fritos_cocinados_hoy
print(f"La base de fritos de hoy en la mañana era de: {base}")

sobras_fritos_hoy = int(input("¿Cuántos fritos sobraron hoy al final del dia? "))
fritos_vendidos_hoy = base - sobras_fritos_hoy
print(f"Los fritos vendidos hoy fueron: {fritos_vendidos_hoy}")

dinero_en_venta_fritos = fritos_vendidos_hoy * 2500

print(f"osea que en el dia de hoy en fritos nos hicimos: {dinero_en_venta_fritos}" )

PAGO_LA_FLACA = 40000
PAGO_MIO = 40000

dinero_nequi = int(input("¿Cuánto dinero se movió por Nequi hoy? "))

print("Tuvimos gastos menores hoy? (si/no)")
if input().lower() == "si":
    print("Cuanto gastamos?")
    gastos_menores = int(input())
else:
    gastos_menores = 0
dinero_fritos_enfisico = ((dinero_en_venta_fritos) - PAGO_LA_FLACA - dinero_nequi - gastos_menores)
print(f"Deberias tener de dinero en fisico de fritos: {dinero_fritos_enfisico}")


