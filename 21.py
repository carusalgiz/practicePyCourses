"""
Программа получает на вход невозрастающую последовательность натуральных чисел.
После этого вводится число X. Все числа во входных данных натуральные и не превышают 200.
Выведите индекс, где окажется число Х.
Если в списке есть элемент с таким значением, то число Х помещается после него.
"""
sequence = list((map(int, input().split())))
X = int(input())
sequence.append(X)
sequence.sort()
print(sequence)
place = 0
i = 0
for i in range(len(sequence)):
    if X >= sequence[i]:
        i +=1
        continue
    else:
        place = i-1
        break
print(place)