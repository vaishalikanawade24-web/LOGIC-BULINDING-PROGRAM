# Check whether a string is a palindrome

s = input("Enter string: ")
print("Palindrome" if s == s[::-1] else "Not Palindrome")
