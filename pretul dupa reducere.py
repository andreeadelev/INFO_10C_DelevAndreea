
pretul=float(input("Dati pretul in lei: "))
reducere=int(input("Dati reducerea in procente: "))
pret_final=pretul*(1-reducere/100)
economie=pretul-pret_final
print(f"Pretul final este de {pret_final:.2f} lei")
print(f"Economia este de {economie:.2f} lei")