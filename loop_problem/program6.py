# Find the sum of first N numbers

n = int(input("Enter N: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Sum =", total)

