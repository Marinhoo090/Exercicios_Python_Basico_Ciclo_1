# Faça uma atualização no código do exercício anterior, agora o programa deve exibir o nome do produto, o valor do desconto e o valor final do produto.

# OUTPUT ESPERADO:

# Produto: FIAT TORO
# Preço: 200000
# Porcentagem de desconto: 15
# O FIAT TORO com 15.0% de desconto custará R$ 170000.0

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

nome = input("Informe o nome do produto: ")
preco = float(input("Digite o valor do produto: "))
desconto = float(input("Digite a porcentagem do desconto: "))

valor_desconto = preco * (desconto/100)
valor_final = preco - valor_desconto

print("informe o nome do produto: ")
print("o produto custa: ",preco)
print("o valor do desconto é: ",valor_desconto)
print("o valor final do produto é: ",valor_final)
