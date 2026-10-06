
putere=int(input("Dati puterea in W: "))
timp=int(input("Dati timpul in ore: "))
energie=putere*timp/1000
print(f"spre achitare {energie:.2f} kWh")
tarif=float(input("Dati tariful in lei/kWh: "))
cost=energie*tarif
print(f"Costul total este de {cost:.2f} lei")