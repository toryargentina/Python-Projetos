# 20/03 - 3.1 Conversão de Moedas

"""
Implemente um programa que converta um valor de Dólares para Reais. Para isso, o usuário
deve informar a Quantidade de Dólares que deseja trocar e a Cotação Atual do dia.
O programa deve processar a conversão multiplicando os valores e exibir o total final
em moeda nacional.
"""

# --------------------------------------------------------

dolares = float(input("Digite a quantidade de doláres a serem convertidos:").replace(",","."))
cotacao = float(input("Digite a cotação: ").replace(",","."))

reais = dolares * cotacao

print(reais)
