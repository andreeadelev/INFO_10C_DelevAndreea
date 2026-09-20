#problema 6
#Se da un numar natural n (n<10000). Sa se afiseze:
n=7896
print("ultima cifra a numarului n este: ", n % 10)
print("penultima cifra a numarului n este: ", (n // 10) % 10)
print("restul si catul impartirii numarului n la 9 sunt: ", n // 9, "si", n % 9)
print("suma cifrelor numarului n este: ", (n // 1000) + ((n // 100) % 10) + ((n // 10) % 10) + (n % 10))
print("rasturnarea numarului n este: ", (n % 10) * 1000 + ((n // 10) % 10) * 100 + ((n // 100) % 10) * 10 + (n // 1000))