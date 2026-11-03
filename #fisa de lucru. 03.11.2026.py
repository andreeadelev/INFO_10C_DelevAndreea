#fisa de lucru

print("Exercitiul 1")
n = int(input(" numarul de locuri (n >= 0): "))
r = list(range(1, n + 1))
print(r)
print(len(r))

print("Exercitiul 2")
a = int(input(" a: "))
b = int(input(" b: "))
r = list(range(a, b + 1, 2))
print(r)

print("Exercitiul 3")
n = int(input(" n: "))
r = list(range(n, -1, -1))
print(r)

print("Exercitiul 4")
cod=int(input(" cod (1-4): "))
from enum import Enum
anotimp = Enum('Anotimp', 'PRIMAVARA VARA TOAMNA IARNA')
print(anotimp(cod).name)
print(anotimp(cod).value) 

print("Exercitiul 5")
N = int(input("n: "))
r = list(range(1, N + 1))
print(r)
print(len(r))

print("Exercitiul 6")
z = int(input(" z: "))
r = list(range(1, 8))
print(z in r)
# Verificarea z in range(1, 8) nu schimbă valoarea lui z deoarece aceasta doar verifică dacă z se află în intervalul.

print("Exercitiul 7")
cod1 = int(input(" cod1 (1-3): "))
cod2 = int(input(" cod2 (1-3): "))
from enum import Enum
Culoare = Enum('Culoare', 'ROSU GALBEN VERDE')
print(Culoare(cod1).name + ", " + Culoare(cod2).name)
print(Culoare(cod1) == Culoare(cod2))

print("Exercitiul 8")
a = int(input(" a: "))
b = int(input(" b: "))
r = list(range(a, b + 1))
print(r[0])
print(r[-1])
print(len(r))
