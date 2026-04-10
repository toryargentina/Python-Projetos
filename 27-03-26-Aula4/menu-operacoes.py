# 4.3 - Menu de Operações

"""
Desenvolva um programa que apresente ao usuário um me2nu com quatro opções de operações
matemáticas básicas. O usuário deverá escolher uma das opções do menu. 
Em seguida, o programa deve solicitar a digitação de dois valores numéricos,
realizar a operação escolhida e exibir o resultado na tela. Após mostrar o resultado,
o programa deve ser encerrado.
"""

# --------------------------------------------------------

print("--- Escolha um operador matemática")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Digite o número da operação desejada: ")

valor1 = float(input("Digite o valor do primeiro número "))
valor2 = float(input("Digite o valor do segundo número "))

if opcao == "1":
    resultado = valor1 + valor2
    print(f"O resultado da soma é {resultado:.2f}")
elif opcao == "2":
    resultado = valor1 - valor2
    print(f"O resultado da subtração é {resultado:.2f}")
elif opcao == "3":
    resultado = valor1 * valor2
    print(f"O resultado da multiplicação é {resultado:.2f}")
elif opcao == "4":
    resultado = valor1 / valor2
    print(f"O resultado da divisão é {resultado:.2f}")
else:
    print("Valor inválido")