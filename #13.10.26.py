#pr1
print("pr1")
nume: str = input("Prenume: ")
print("primul caracter este:", nume[0])
print( "Lungimea etse: " , len(nume))

print("pr2")
litera: str = input("Literă: ")
print(litera in "aeiou")

print("pr3")
prenume: str = input("Prenume: ")
clasa: str = input("Clasa: ")
print("Prenume: " + prenume + ", clasa: " + clasa)
print("Lungimea etichetei este:", len("Prenume: " + prenume + ", clasa: " + clasa))

print("pr4")
raspuns: str = input("Participi? ")
print(raspuns == "da")

print("pr5")
a: str = input("Text 1: ")
b: str = input("Text 2: ")
print(a == b)
print(len(a) == len(b))


print("pr6")
nume: str = input("Nume: ")
r: str = input("Participi? ")
acces: bool = nume != "" and r == "da"
print(acces)

print("pr7")
prenume: str = input("Prenume: ")
nume: str = input("Nume: ")
initiala_1: str = prenume[0]
initiala_2: str = nume[0]
print(initiala_1 + "." + initiala_2 + ".")

print("pr8")
nume: str = input("Nume: ")
print("Salut, " + nume)
r: str = input("Participi? ")
participa: bool= r=="da"
print(participa)


#probleme pentru acasa
print("probleme pentru acasa")
print("pr1")

cuvant=input("Introduceti un cuvant nevid:")
lungime=len(cuvant)
primul_caracter=cuvant[0]
ultimul_caracter=cuvant[-1]
print(lungime,primul_caracter, ultimul_caracter)

print("pr2")
text=("Introduceti un text")
este_vid=(text== "")
print(este_vid)

print("pr3")
text=input("introduceti textul:")
rezutat_t3= 3 <= len(text) <= 10
print(rezutat_t3)

print("pr4")
litera= input("intriduceti o litera mica:")
rezultat_t4= (litera =="a") or (litera =="e") or (litera =="i") or (litera =="o") or (litera =="u")
print(rezultat_t4)
