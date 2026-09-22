#PROBLEMA 1

# Exemple pentru int
x = 5
y = 10
print(type(x))
print(type(y))

# Exemple pentru float
a = 3.14
b = 2.71
print(type(a))
print(type(b))

# Exemple pentru bool
T = True
F = False
print(type(T))
print(type(F))

# Exemple pentru str
s1 = "Hello"
s2 = "World"
print(type(s1))
print(type(s2))


#PROBLEMA 2
m = float(input("Introdu masa: "))
v = float(input("Introdu viteza: "))
Ec = m * v**2 / 2
print(f"Energia cinetică este: {Ec}")   


#PROBLEMA 3
import math  
x = float(input("Introdu un număr real: "))
print(f"Valoarea absolută: {abs(x)}")  # Afișează valoarea absolută a lui x
print(f"Partea întreagă (floor): {math.floor(x)}")  # Afișează partea întreagă inferioară a lui x
print(f"Partea întreagă (ceil): {math.ceil(x)}")  # Afișează partea întreagă superioară a lui x
print(f"Rotunjire (round): {round(x, 2)}")  # Afișează valoarea rotunjită a lui x cu 2 zecimale