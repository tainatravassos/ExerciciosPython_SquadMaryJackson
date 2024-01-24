# 3. Crie um dicionário representando um carrinho de compras. Adicione produtos (chaves) e quantidades (valores) ao carrinho. Calcule o total do carrinho de compra.


carrinho_de_compras = {}

carrinho_de_compras["Produto1"] = 2
carrinho_de_compras["Produto2"] = 1
carrinho_de_compras["Produto3"] = 3


precos = {
    "Produto1": 10.0,
    "Produto2": 5.0,
    "Produto3": 8.0
}

total_carrinho = sum(qtd * precos[produto] for produto, qtd in carrinho_de_compras.items())

print("Carrinho de Compras:")
for produto, qtd in carrinho_de_compras.items():
    print(f"{produto}: {qtd} unidades")

print(f"\nTotal do Carrinho: R$ {total_carrinho:.2f}")
