#10/04 - 6.3 Investimento

"""
Um investimento inicial de R$P cresce a uma taxa de juros anual i, durante t anos. Sabe-se
que M = P * e^(i*t). Crie um programa (com função) que:
a) Receba o valor inicial (P)
b) Receba a taxa de juros anual (i, em decimal, ex: 0.05 para 5%)
c) Receba o tempo em anos (t)
d) Calcule o montante final usando math.exp()
"""

# --------------------------------------------------------

import math

def calcular_montante():
    p = float(input("Digite o valor inicial (P): "))
    i = float(input("Digite a taxa de juros (ex: 0.05 para 5%): "))
    t = float(input("Digite o tempo em anos (t): "))

    montante = p * math.exp(i * t)

    print(f"O montante final será de: R$ {montante:.2f}")

calcular_montante()