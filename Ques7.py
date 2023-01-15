n = 10
a, b = 0, 1
sum = 0
print(a)
print(b)
sum = a + b
for i in range(2, n):
    c = a + b
    print(c)
    sum += c
    a, b = b, c

average = sum / n
print("Average:", average)
