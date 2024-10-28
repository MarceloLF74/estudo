# Tabuada do 7
for i in range(1, 11):  # De 1 a 10
    resultado = 7 * i
    if resultado % 4 == 0:  # Verifica se o resultado é múltiplo de 4
        continue  # Pula para a próxima iteração
    print(f"7 x {i} = {resultado}")