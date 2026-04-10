# 03/04 - Soma dos quadrados 

"""
Escreva um programa que receba um número inteiro n e calcule a soma dos quadrados dos
números até n-1. Exemplo: se n for igual a 3, seu programa deve dar o resultado da soma
dos números 1*1 + 2*2.
"""

# --------------------------------------------------------

n = int(input("Digite um número inteiro: "))

soma = 0

for i in range(1, n):
    soma += i ** 2

print(soma)