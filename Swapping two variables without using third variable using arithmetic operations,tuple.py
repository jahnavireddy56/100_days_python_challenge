# Take input from the user
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

# Swap without using a third variable (arithmetic method)
a = a + b
b = a - b
a = a - b

# Display the result
print("After swapping:")
print("a =", a)
print("b =", b)
#swapping using tuple unpacking
a = int(input("Enter a: "))
b = int(input("Enter b: "))

a, b = b, a

print("Swapped values: a =", a, ", b =", b)