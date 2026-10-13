#pr1
print("pr1")
nume = input("Prenume: ")
print("Prima literă a prenumelui este:", nume[0])
print("Lungimea prenumelui este:", len(nume))

print("pr2")
litera = input("Literă: ")
print(litera in "aeiou")

print("pr3")
prenume = input("Prenume: ")
clasa = input("Clasa: ")
print("Prenume: " + prenume + ", clasa: " + clasa)
print("Lungimea etichetei este:", len("Prenume: " + prenume + ", clasa: " + clasa))

print("pr4")
raspuns = input("Participi? ")
print(raspuns == "da")

print("pr5")
a = input("Text 1: ")
b = input("Text 2: ")
print(a == b)
print(len(a) == len(b))


print("pr6")
nume = input("Nume: ")
r = input("Participi? ")
acces = nume != "" and r == "da"
print(acces)

print("pr7")
prenume = input("Prenume: ")
nume = input("Nume: ")
initiala_1 = prenume[0]
initiala_2 = nume[0]
print(initiala_1 + "." + initiala_2 + ".")

print("pr8")
nume = input("Nume: ")
print("Salut, " + nume)
r = input("Participi? ")
participa= bool(r)
print(participa == True)




