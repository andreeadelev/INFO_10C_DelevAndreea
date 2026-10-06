#tema pentru acasa 12.10.2026
#problema 1

n = int(input("Introduceti un numar intreg de zile (n >= 0): "))
ore= n * 24
minute= n * 24 * 60
print(f"Numarul de ore este: {ore} ore , iar numarul de minute este: {minute} minute")

#problema 2
masa_1=float(input("Introduceti masa primului obiect in kg: "))
masa_2=float(input("Introduceti masa celui de-al doilea obiect in kg: "))
masa_totala_kg= masa_1 + masa_2
print(f"Masa totala este: {masa_totala_kg:.2f} kg")
print(f"Masa totala este: {masa_totala_kg * 1000:.2f} g")

#problema 3
distanta_km = float(input("Introduceti distanta parcursa in km: "))
consum_l_100km = float(input("Introduceti consumul in l/100km: "))
consum_l_km = consum_l_100km / 100
consum_necesar_l = consum_l_km * distanta_km
print(f"Consumul total de combustibil este: {consum_necesar_l:.2f} litri")

#problema 4
n= int(input("Introduceti un numar intreg de minute (N >= 0): "))
ore_complete= n // 60
minute_ramase= n % 60
print(f"Numarul de ore complete este: {ore_complete}, iar numarul de minute ramase este: {minute_ramase}")