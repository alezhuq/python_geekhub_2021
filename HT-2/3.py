# 3. Написати скрипт, який видалить пусті елементи із списка. Список можна "захардкодити".

hardcoded_sample = [(), (), (), (), ('',), ('a', 'b'), {}, ('a', 'b', 'c'), 'd', '', [], (), {}]

i = 0

while i < len(hardcoded_sample):
    if not len(hardcoded_sample[i]):
        hardcoded_sample.pop(i)
        continue
    i = i + 1


print(hardcoded_sample)
