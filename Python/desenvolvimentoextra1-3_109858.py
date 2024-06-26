"""
Proz - Talento Cloud
Introdução à Programação com foco em Front-End - Turma 28
Preparação para HTML e CSS
Desenvolvimento Extra 1.3 - 109858
Emily Matias

Enunciado:
Uma nova loja de cosméticos abriu no seu bairro e pediram para você elaborar um sistema que imprime na tela na frente da loja os novos produtos que chegaram.
O sistema da loja já tem um array com os produtos, você precisa apenas imprimir eles no terminal, um por um.
Como desafio opcional, tente imprimir cada produto com a frase "Temos [produto] à venda!" (ex. "Temos máscaras faciais à venda!"). 
lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores']
"""

# Array de produtos
lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores']

# Laço para imprimir o array
for produto in lista_produtos:
  print(f"Temos {produto} à venda!")