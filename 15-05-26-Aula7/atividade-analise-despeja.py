# BASE DE DADOS FORNECIDA

despesas = [1200, 800, 450, 300, 150]
pib_crescimento = [2.1, 3.5, -0.5, 1.8, 2.9]
precos = [10, 20, 30, 40]
cesta = ["pao", "leite", "pao", "ovos", "leite", "pao"]
rendas = [1200, 2500, 800, 3000, 1500, 700]


# 1. ANÁLISE DE DESPESAS MENSAIS

print("--- 1. Análise de Despesas Mensais ---")

total_gasto = sum(despesas)
maior_despesa = max(despesas)
menor_despesa = min(despesas)

print(f"Total gasto: R$ {total_gasto}")
print(f"Maior valor gasto: R$ {maior_despesa}")
print(f"Menor valor gasto: R$ {menor_despesa}")
print()


# 2. ANÁLISE DO PIB
print("--- 2. Análise do Crescimento do PIB ---")

anos_negativos = 0
soma_pib = 0
anos_acima_2 = []

for taxa in pib_crescimento:
    soma_pib += taxa
    
    if taxa < 0:
        anos_negativos += 1
        
    if taxa > 2.0:
        anos_acima_2.append(taxa)

media_pib = soma_pib / len(pib_crescimento)

print(f"Quantidade de anos com crescimento negativo: {anos_negativos}")
print(f"Média das taxas de crescimento: {media_pib:.2f}%")
print(f"Taxas superiores a 2%: {anos_acima_2}")
print()


# 3. REAJUSTE DE PREÇOS (INFLAÇÃO)
print("--- 3. Reajuste de Preços ---")

precos_reajustados = []

for preco in precos:
    novo_preco = preco * 1.10
    precos_reajustados.append(round(novo_preco, 2))

print(f"Preços originais: {precos}")
print(f"Preços reajustados (10%): {precos_reajustados}")
print()


# 4. CONTABILIZAÇÃO DA CESTA DE COMPRAS

print("--- 4. Análise da Cesta de Compras ---")

produtos_unicos = []
for item in cesta:
    if item not in produtos_unicos:
        produtos_unicos.append(item)

maior_quantidade = 0
item_mais_consumido = ""

for produto in produtos_unicos:
    quantidade = cesta.count(produto)
    print(f"O produto '{produto}' aparece {quantidade} vezes.")
    
    if quantidade > maior_quantidade:
        maior_quantidade = quantidade
        item_mais_consumido = produto

print(f"Item mais consumido: '{item_mais_consumido}' (comprado {maior_quantidade} vezes).")
print()



# 5. CLASSIFICAÇÃO DE RENDAS
print("--- 5. Classificação de Rendas ---")

baixa_renda = []
media_renda = []
alta_renda = []

for renda in rendas:
    if renda <= 1000:
        baixa_renda.append(renda)
    elif renda <= 2000:
        media_renda.append(renda)
    else:
        alta_renda.append(renda)

print(f"Baixa renda: {baixa_renda} (Total: {len(baixa_renda)} indivíduos)")
print(f"Média renda: {media_renda} (Total: {len(media_renda)} indivíduos)")
print(f"Alta renda: {alta_renda} (Total: {len(alta_renda)} indivíduos)")