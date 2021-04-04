from sys import getsizeof


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = []
for i in range(len(src) - 1):
    if src[i] < src[i+1]:
        result.append(src[i+1])
print(result)
print('Размер списка', getsizeof(result))


# надо как-то использовать материалы урока
def bigger_element_gen(src_list):
    for num in range(len(src_list) - 1):
        if src_list[num] < src_list[num + 1]:
            yield src_list[num + 1]


print(*bigger_element_gen(src))
print('Размер генератора', getsizeof(bigger_element_gen(src)))
# Честно говоря, разница минимальна
