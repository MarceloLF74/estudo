#exercicio1
adicionar_dez = lambda x: x + 10
print(adicionar_dez(5))

#exercicio2
maior_que_20 = lambda x: x > 20
print(maior_que_20(25))
print(maior_que_20(15))

#exercicio3
multiplicar_por_tres = lambda x: x * 3
print(multiplicar_por_tres(4))

#exercicio4
texto_maiusculas = lambda x: x.upper()
print(texto_maiusculas('olá'))

#exercicio5
subtrair_cinco = lambda x: x - 5
print(subtrair_cinco(10))

#exercicio6
eh_negativo = lambda x: x < 0
print(eh_negativo(-3))
print(eh_negativo(2))

#exercicio6.1
calculo_media = lambda x, y: (x + y) / 2
print(calculo_media(3, 16.7))

#exercicio7
substituir_a_por_o = lambda texto: texto.replace('a', 'o')
print(substituir_a_por_o('Viva a vida muito intensamente'))