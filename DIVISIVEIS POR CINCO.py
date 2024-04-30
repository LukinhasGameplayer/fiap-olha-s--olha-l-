a = int(input('Digite o primero número: '))
b = int(input('Digite o segundo número: '))


if a>b:
    tmp = a
    a = b
    b = tmp

for i in range(a, b+1):
    if i % 5 == 0:
        print(i)


xorume ao quadrado

