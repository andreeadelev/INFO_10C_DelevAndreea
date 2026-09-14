#Structura fisierului
#Delev Andreea, clasa 10C
#Lectia 3 - Operatori in python

#1. Calculati aria si perimetrul unui dreptunghi
l=8
L=13
aria =  l*L
perimetru = 2*(L+l)
print( "1. aria=", aria)
print( "1. perimetru =, perimetru)

Pentru 95 minute, afisati cate ore intregi si cate minute raman
minute = 95 
ore=minute //60
minute_ramase= minute %60
print("2." ore, "ore si", minute_ramase, "minute")

#3. Pentru un numar n, afisati TRUE daca este par si FALSE daca este impar
n=int(input ("3. introduceti numarul n: "))
print(n%2==0)

#4. Scrieti 3 expresii in care parantezele schimba rezultatul
print("4. Fara paranteze:", 2+3*4)
print("4. Cu paranteze:", (2+3)*4)

print("4. Fara paranteze:", 10-2*3 )
print("4. Cu paranteze:", (10-2)*3 )

print("4. Fara paranteze:", 20/5+3 )
print("4. Cu paranteze:",20/(5+3)  )

#5. Creati un exemplu propriu cu and, or sau not si explicati-l in comentariu
a=8
b=3
rezultat=( a>5 and b<5) or not (a==10)
print("5.", rezultat)

#Explicatie:
#a>5 este True, iar b<5 este True.
#True and true este True.
#a==10 este fals, iar not false este true.
#True or True este true.
