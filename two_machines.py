k = int(input('k: ')) # смена
a, x = map(int, input("a, x: ").split()) # a - время подготовки первого станка, x - деталей в минуту
b, y = map(int, input("b, y: ").split()) # b - время подготовки второго станка, y - деталей в минуту

A_a = (k - a) * x # производительность за время работы k - a
A_b = (k - b) * y # производительность за время работы k - b

if A_a > A_b:
    all_details = (k - a) * x + (k - a - b) * y
else:
    all_details = (k - b) * y + (k - a - b) * x

print(all_details)