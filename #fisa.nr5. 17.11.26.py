#fisa.nr5

print("pr1")
a: int = int(input("Introduceti valoarea lui a: "))
b: int = int(input("Introduceti valoarea lui b: "))
x: int = int(input("Introduceti valoarea lui x: "))
locuri = range(a, b + 1)
print(x in locuri)
print(len(locuri)) 

print("pr2")
a: int = int(input("Introduceti valoarea lui a: "))
b: int = int(input("Introduceti valoarea lui b: "))
x: int = int(input("Introduceti valoarea lui x: "))
locuri = range(a, b + 1, 2)
print(list(locuri))
print(x in locuri)
# Un număr dintre capete poate lipsi din range dacă pasul nu este 1, ceea ce înseamnă că nu toate valorile din interval sunt incluse.

print("pr3")
from enum import Enum
class Club(Enum):
    ROBOTICA = 1
    ARTA = 2
    SPORT = 3
cod: int = int(input("Introduceti codul clubului: "))
Club = Club(cod)
print(f" {Club.name}")
print(f" {Club == Club.ROBOTICA}")

print("pr4")
Masa = float
m = float(input("Introduceti masa in kg: "))
print(f"Masa este: {m:.2f} kg")
print(f"{0 < m <= 5}")

print("pr5")
a: int = int(input("Introduceti valoarea lui a: "))
b: int = int(input("Introduceti valoarea lui b: "))
x: int = int(input("Introduceti valoarea lui x: "))
print(x in range(a, b + 1))

print("pr6")
Temperatura = float
t: Temperatura = float(input("Introduceti temperatura: "))
print(f"Temperatura este: {t}")
print(f"{18 <= t <= 25}")
print(f"{type(t)}")
# range(18, 26) nu descrie toate temperaturile reale deoarece range generează doar numere întregi, iar temperatura poate fi un număr float.

print("pr7")
from enum import Enum
class Stare(Enum):
    NOU = "nou"
    LUCRU = "lucru"
    GATA = "gata"
stare: Stare = Stare(input("Introduceti starea (nou, lucru, gata): "))
print(f"Numele stării: {stare.name}")
print(f"{stare.value}")
print(f"Starea este GATA: {stare == Stare.GATA}")

print("pr8")
a: int = int(input("Introduceti valoarea lui a: "))
b: int = int(input("Introduceti valoarea lui b: "))
x: int = int(input("Introduceti valoarea lui x: "))
r: range = range(a, b + 1)
print(f" {len(r)}")
print(f" {type(r)}")
print(f" {x in r}")
