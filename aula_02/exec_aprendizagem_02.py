num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

if num1 < num2 and num2 < num3:
    print(f'O número {num3} é o maior deles')
elif num1> num2 and num2 > num3:
    print(f'O número {num1} é o maior deles')
else:
    print(f'O número {num2} é o maior deles')