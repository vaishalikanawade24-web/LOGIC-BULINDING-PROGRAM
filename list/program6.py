# Remove duplicates from a list

lst = [1, 2, 2, 3, 4, 4, 5]
new_lst = []
for x in lst:
    if x not in new_lst:
        new_lst.append(x)
print("Without duplicates =", new_lst)
