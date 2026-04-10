#10/04 - 5.2  Habitantes

"""
 Supondo que a população de um país A seja da ordem de 80.000 habitantes com uma taxa
 anual de crescimento de 3% e que a população de B seja de 200.000 habitantes com uma
 taxa de crescimento de 1,5%. Faça um programa que calcule e escreva o número de anos
 necessários para que a população do país A ultrapasse ou iguale a população do país B,
 mantidas as taxas de crescimento.
"""

# --------------------------------------------------------

populacaoA = 80000
populacaoB = 200000
anos = 0

while populacaoA < populacaoB:
    populacaoA += populacaoA * 0.03
    populacaoB += populacaoB * 0.015
    anos += 1

print(anos)