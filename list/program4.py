# Find the minimum element in a list

lst = [10, 20, 30, 40, 50]
min_val = lst[0]
for x in lst:
    if x < min_val:
        min_val = x
print("Minimum =", min_val)
