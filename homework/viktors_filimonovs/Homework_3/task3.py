import math

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

arith_mean = (num1 + num2) / 2
geom_mean = math.sqrt(num1 * num2)

print("Arithmetic mean:", arith_mean)
print("Geometric mean:", geom_mean)
