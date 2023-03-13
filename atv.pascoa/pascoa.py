# Definição dos valores dos ovos de páscoa e adicionais
ovo_pequeno = 7.80
ovo_medio = 12.90
ovo_grande = 23.95
chocolate_preto = 9.67
chocolate_branco = 4.50
chocolate_ao_leite = 9.32
kitkat = 4.67
mms = 5.43
presente = 2.50
fornecer = 5.00
pagamento_cartao = 3.30
desconto_dinheiro_pix = 0.10

# Entrada de dados pelo usuário
tamanho = input("Qual o tamanho do ovo? (P - pequeno / M - médio / G - grande): ")
sabor = input("Qual o sabor do ovo? (P - chocolate preto / B - chocolate branco / L - chocolate ao leite): ")
recheio1 = input("Deseja adicionar um recheio? (S - sim / N - não): ")
recheio2 = "N"
if recheio1 == "S":
    recheio2 = input("Deseja adicionar um segundo recheio? (S - sim / N - não): ")
adicionais = input("Deseja adicionar algum adicional? (S - sim / N - não): ")
presente_ou_fornecer = input("É um presente ou para consumo próprio? (P - presente / F - fornecer): ")
forma_pagamento = input("Qual a forma de pagamento? (C - cartão de crédito / D - dinheiro / P - PÍX): ")
quantidade = int(input("Qual a quantidade de ovos? "))

# Cálculo do valor total do ovo
valor_ovo = 0
if tamanho == "P":
    valor_ovo = ovo_pequeno
elif tamanho == "M":
    valor_ovo = ovo_medio
elif tamanho == "G":
    valor_ovo = ovo_grande

if sabor == "P":
    valor_ovo += chocolate_preto
elif sabor == "B":
    valor_ovo += chocolate_branco
elif sabor == "L":
    valor_ovo += chocolate_ao_leite

if recheio1 == "S":
    valor_ovo /= 2
if recheio2 == "S":
    valor_ovo /= 2

if adicionais == "S":
    valor_ovo += kitkat
    valor_ovo += mms

if presente_ou_fornecer == "P":
    valor_ovo += presente
elif presente_ou_fornecer == "F":
    valor_ovo += fornecer

valor_total = valor_ovo * quantidade

if forma_pagamento == "C":
    valor_total += pagamento_cartao
elif forma_pagamento == "D" or forma_pagamento == "P":
    valor_total *= (1 - desconto_dinheiro_pix)


print(f"Valor total dos ovos de páscoa: R${valor_total:.2f}")