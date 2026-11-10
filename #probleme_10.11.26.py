#probleme_10.11.26

print("pr1")
prenume: str = input("Introdu prenumele: ")
varsta: int = int(input("Introdu vârsta (≥ 0): "))
print(f"Prenumele este {prenume} și vârsta este {varsta}.")

print("pr2")
stoc: int = int(input("Introdu stocul (≥ 0): "))
numar_primit: int = int(input("Introdu numărul primit (≥ 0): "))
stoc += numar_primit
print(f"Noul stoc este {stoc}.")

print("pr3")
a=5
b=10
print(f"inainte de schimbare: a={a}, b={b}")
a , b = b, a 
print(f"dupa schimare: a={a}, b={b}")
# a și b sunt variabile care stochează valori întregi. Înainte de schimbare, a are valoarea 5 și b are valoarea 10. După schimbare, valorile lor sunt inversate: a devine 10 și b devine 5.

print("pr4")
PRET_CAIET=8.50
n=int(input("Introdu numărul de caiete (≥ 0): "))
total=n*PRET_CAIET
print(f"Totalul este {total:.2f}.")
# Numele cu majuscule este doar o convenție pentru a indica faptul că valoarea este considerată constantă.

print("pr5")
varsta: int = int(input("Introdu vârsta (≥ 0): "))
varsta_peste_un_an: int = varsta + 1
print(f"Vârsta peste un an este {varsta_peste_un_an}.")
# Adnotarea indică tipul de date pe care o variabilă ar trebui să îl aibă, dar nu efectuează nicio conversie. Conversia transformă valoarea într-un alt tip de date.
# În acest caz, `varsta: int` este o adnotare care sugerează că `varsta` ar trebui să fie un întreg, iar `int(input(...))` efectuează conversia valorii introduse de utilizator într-un întreg.

print("pr6")
Distanta=float
d: Distanta = float(input("Introdu distanța (≥ 0): "))
print(f"Distanța este {d:.1f} , {type(d)}.")

print("pr7")

Lungime = float
a: Lungime = float(input("Introdu lungimea a (≥ 0): "))
b: Lungime = float(input("Introdu lungimea b (≥ 0): "))
aria: float = a * b
perimetrul: float = 2 * (a + b)
print(f"Aria este {aria:.2f} și perimetrul este {perimetrul:.2f}.")

print("pr8")
t: float = input("Introdu temperatura: ")
print(f"Tipul inițial al lui t este {type(t)}.")
t = float(t)
print(f"Tipul după conversie al lui t este {type(t)} și valoarea este {t}.")
# Primul tip este str deoarece funcția input() returnează întotdeauna un șir de caractere "str", indiferent de adnotarea tipului. 
# Adnotarea tipului nu efectuează nicio conversie; ea doar sugerează ce tip ar trebui să aibă variabila. Conversia efectivă la float se face prin  funcția float().

