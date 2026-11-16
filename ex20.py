
dinheiro = float(input("Quanto dinheiro você tem? R$ "))
print("Lanches: 1-Lanche R$15 | 2-Suco R$8 | 3-Combo R$20")
pedido = input("O que você quer? (1/2/3): ")
if pedido == "1":
    preco = 15
elif pedido == "2":
    preco = 8
elif pedido == "3":
    preco = 20
else:
    print("Pedido inválido!")
    exit()
if dinheiro >= preco:
    troco = dinheiro - preco
    print(f" Pode levar! Troco: R$ {troco:.2f}")
else:
    falta = preco - dinheiro
    print(f" Falta R$ {falta:.2f}")
