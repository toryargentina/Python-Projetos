#10/04 - 5.3 Calcula Média

"""
Escreva um programa que calcule a média dos números digitados pelo usuário.
O programa deve calcular a média quando o usuário digitar o número zero.
"""

# --------------------------------------------------------

soma = 0
quantidade = 0

numero = int(input("Digite um número (0 para encerrar): "))

while numero != 0:
    soma += numero
    quantidade += 1
    numero = int(input("Digite um número (0 para encerrar): "))

print(soma / quantidade)