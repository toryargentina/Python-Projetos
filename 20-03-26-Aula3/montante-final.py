# 20/03 - 3.2 Montante Final

"""
Implemente um programa que calcule o Montante Final de um investimento em Juros Simples.
Para isso, o usuário deve informar o Capital Inicial, a Taxa de Juros (em porcentagem)
e o Tempo (em meses). Sabe-se que a fórmula para o cálculo é M = C * (1 + i * n), onde
a taxa deve ser convertida para valor decimal.
"""

# --------------------------------------------------------

capital = float(input("Digite o Capital: ").replace(",","."))

juros = float(input("Digite a Taxa de Juros:").replace(",",".")) /100
tempo = float(input("Digite o Tempo:").replace(",","."))

montante = capital * (1 + juros * tempo )

print("O montante final será:" , montante )