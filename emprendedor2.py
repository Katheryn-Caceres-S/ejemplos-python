import math as m


# 𝑈𝑡𝑖𝑙𝑖𝑑𝑎𝑑𝑒𝑠 = 𝑃 * 𝑈 − 𝐺𝑇

""" 
P1: Precio de Suscripción normal
p2: Precio de suscripcion premiun 50% mayor
U1: Número de Usuarios normales
U2: Numero de usuarios premiun
GT: Gastos Totales 
"""

p1 = float(input("Ingresa el precio de suscripcion normal : "))
p2 = (p1 * 1.5)
u1 = float(input ("Ingresa el numero de usuarios Normal: "))
u2 = float(input ("Ingresa el numero de usuarios Premiun : "))
gt = float(input ("Ingresa los gastos totales : "))


## utilidad
ut = ((p1 + p2) * (u1 + u2) - gt)

print(f"La utilidad es de : {ut}")