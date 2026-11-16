distancia = input("Prefere atacar de longe (1) ou de perto (2)? ")
if distancia == "1":
    tipo = input("Você usa Magia (A) ou Arco (B)? ").upper()
    if tipo == "A":
        print(" Você é um MAGO!")
    else:
        print(" Você é um ARQUEIRO!")
else:
    arma = input("Você usa Espada (A) ou Adagas (B)? ").upper()
    if arma == "A":
        print(" Você é um GUERREIRO!")
    else:
        print(" Você é um ASSASSINO!")
