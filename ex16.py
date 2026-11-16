mesada = float(input("Quanto você guardou? R$ "))
preco_jogo = float(input("Preço do jogo que você quer? R$ "))
if mesada >= preco_jogo:
    troco = mesada - preco_jogo
    print(f" Dinheiro suficiente! Troco: R$ {troco:.2f}")
else:
    falta = preco_jogo - mesada
    print(f" Falta R$ {falta:.2f}")
