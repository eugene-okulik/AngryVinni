import math

katet1 = float(input("Enter the first leg: "))
katet2 = float(input("Enter the second leg: "))

hypotenuse = math.sqrt(katet1**2 + katet2**2)
area = (katet1 * katet2) / 2

print("Hypotenuse:", hypotenuse)
print("Triangle area:", area)
