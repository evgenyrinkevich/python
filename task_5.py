src = [2, 2, -2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# Короткое решение
result = [el for el in src if src.count(el) == 1]
print(result)

# Более быстое решение
unique_nums = set()
tmp = set()
for el in src:
    if el not in tmp:
        unique_nums.add(el)
    else:
        unique_nums.discard(el)
    tmp.add(el)
unique_nums_ord = [el for el in src if el in unique_nums]
print(unique_nums_ord)
