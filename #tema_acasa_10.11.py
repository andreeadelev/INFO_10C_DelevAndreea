#tema_acasa_10.11.26

print("pr1")
#citeste stocul si actualizeaza cu o cantitate primita
stoc=int(input("Introduceti stocul initial:"))
cantitate=int(input("Introduceti cantitatea primita:"))
stoc +=cantitate
print("stocul actualizat este :", stoc)

print("pr2")
a=5
b=10
print(f"inainte de schimbare: a={a}, b={b}")
a , b = b, a 
print(f"dupa schimare: a={a}, b={b}")

print("pr3")
TARIF = 3.0
cantitate = 5
cost_total = cantitate * TARIF
print(f"Pentru o cantitate de {cantitate}, costul total este: {cost_total}")

print("pr4")
valoare_text = "75.5"
m = float(valoare_text)
if m > 0:
    print("Masa este valida:", m)
else:
   print("Eroare: Masa trebuie sa fie mai mare ca 0")
