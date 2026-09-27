
print("Introduceți coordonatele punctului A (x₁, y₁):")
x1 = float(input("x₁: "))
y1 = float(input("y₁: "))
print("Introduceți coordonatele punctului B (x₂, y₂):")
x2 = float(input("x₂: "))
y2 = float(input("y₂: "))
import math
d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"Distanța dintre punctele A și B este: {d}")
