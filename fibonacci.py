print('Fibonacci')
num_termo = int(input('Entre com o número de termos: '))
a = 0
b = 1
print(a, end = ',')
print(b, end = ',')
i = 1

while i <= num_termo - 2:
    c = a + b
    print(c, end = ',')
    # a = b
    # b = c
    a, b = b, c
    i = i + 1
