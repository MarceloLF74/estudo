a = int(input('Digite o lado a do triângulo: '))
b = int(input('Digite o lado b do triângulo: '))
c = int(input('Digite o lado c do triângulo: '))

if a == b and b == c and c == a:
    print('O triângulo é EQUILÁTERO(três lados iguais)')
elif a != b and b!= c and c != a:
    print('O triângulo é ESCALENO(todos os lados são diferentes)')
else:
    print('O triâgulo é ISÓCELES(dois lados iguais)')
