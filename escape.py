#Velocidad de Escape en [m/s]. Ve

#constante gravitacional en [m/s2]
g = float (input("Introduce el valor de la Constante Gravitacional g en m/s2 : "))

# radio del planeta en [m].
r = int (input ("Introduce el radio r del planeta en kilometros : "))

# 𝑉 𝑒 =  raiz 2 g r

ve =  (2 * g * (r*1000)) ** 0.5

print (f"La vecolidad es de {ve:.1f}")