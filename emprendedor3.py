import math as m


# 𝑈𝑡𝑖𝑙𝑖𝑑𝑎𝑑𝑒𝑠 = 𝑃 * 𝑈 − 𝐺𝑇

""" 
P: Precio de Suscripción 
U: Número de Usuarios normales
GT: Gastos Totales 
Ut_anterior : utilidad año anterior
Ut_actual :  utilidad actual
r = razon entre utilidad actual y anterior
"""

print("IMPORTANTE: Digita solo números, sin caracteres especiales y utiliza un punto como separador decimal.")
p = float(input("Ingresa el precio de suscripcion : "))
u = float(input ("Ingresa el numero de usuarios Normal: "))
gt = float(input ("Ingresa los gastos totales : "))
ut_anterior = float (input("Ingresa las utilidades del año anterior : "))

## utilidad
ut_actual = ((p * u) - gt)
r = ut_anterior / ut_actual

print(f"La utilidad actual es de : {ut_actual} \n y la razon entre la utilidad actual y la del año anterior es de {r:.2f}")