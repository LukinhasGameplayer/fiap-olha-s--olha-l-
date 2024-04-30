num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
total = num1
par = 0
impar = 0


while total <= num2:
    if total % 2 == 0:
        par += 1
    else:
        impar += 1
    total += 1
print(f'São {par} pares e {impar} impares' )




