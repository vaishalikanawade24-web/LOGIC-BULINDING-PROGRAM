# Reverse a string

# s = int (input("Enter string: "))
# print("Reversed =", s[::-1])

s = input("Enter string: ")
rev = ""
for ch in s:
    rev = ch + rev
print("Reversed =", rev)
