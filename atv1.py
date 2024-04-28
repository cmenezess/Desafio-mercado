# Faça um Programa que registrará as vendas de uma loja. Cada venda
# conterá:

# Nome do Comprador
# Preço da Compra

# A cada venda o programa deve perguntar: “Deseja registrar mais uma venda?”

# O usuário deve responder com “S” ou “N” para a pergunta. Essa resposta deve ser
# tratada, não permitindo números ou palavras com mais uma letra. Além disso, o
# programa deve aceitar a resposta independentemente dela ser maiúscula ou
# minúscula.

# Ao final do programa, ele deve mostrar o faturamento total do dia e qual foi o
# comprador que gastou mais na loja.
total_vendas = {}
total = 0
comprador_maior_gasto = ""
maior_total_gasto = 0

while True:
    nome = input("Nome do comprador: ")
    preco = float(input("Preço da compra: R$"))
    total += preco
    
    if nome in total_vendas:
        total_vendas[nome] += preco
    else:
        total_vendas[nome] = preco
    
    if total_vendas[nome] > maior_total_gasto:
        maior_total_gasto = total_vendas[nome]
        comprador_maior_gasto = nome

    cont = input("Deseja registrar mais uma venda? [S/N]: ").upper()
    if cont == "N":
        break
    elif cont != "S":
        print("Resposta inválida. Por favor, responda apenas com 'S' ou 'N'.")
        continue

print(f"Faturamento total do dia: {total}")
print(f"O comprador que gastou mais na loja foi: {comprador_maior_gasto}")
print(f"Valor total gasto pelo comprador que gastou mais na loja: R${maior_total_gasto}")
