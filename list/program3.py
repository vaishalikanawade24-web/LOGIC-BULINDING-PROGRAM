# Find the maximum element in a list

lst = [10, 20, 30, 40, 50]
max_val = lst[0]
for x in lst:
    if x > max_val:
        max_val = x
print("Maximum =", max_val)
