#PROVOCARE
# „calculator de triunghi dreptunghic” care citește catetele, calculează ipotenuza și cele două unghiuri ascuțite. Folosește math.hypot(), math.atan2() și math.degrees().
import math

# Citirea catetelor
a = float(input("Introdu lungimea primei catete: "))
b = float(input("Introdu lungimea celei de-a doua catete: "))
c = math.hypot(a, b)

# Calculul unghiurilor ascuțite
U1 = math.degrees(math.atan2(a, b))
U2 = math.degrees(math.atan2(b, a))
print(f"Ipotenuza este: {c}")
print(f"Unghiul ascuțit 1 este: {U1} grade")
print(f"Unghiul ascuțit 2 este: {U2} grade")
