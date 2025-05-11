import math as m


# 𝑈𝑡𝑖𝑙𝑖𝑑𝑎𝑑𝑒𝑠 = 𝑃 * 𝑈 − 𝐺𝑇

""" 
P: Precio de Suscripción
U: Número de Usuarios
GT: Gastos Totales 
"""

p = int(input("Ingresa el precio de suscripcion : "))
u = int(input ("Ingresa el numero de usuarios : "))
gt = int(input ("Ingresa los gastos totales : "))

#area= (m.sqrt())

## utilidad
ut = (p * u - gt)

print(f"La utilidad es de : {ut}")