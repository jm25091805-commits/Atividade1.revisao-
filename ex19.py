
resposta = input("Você tirou nota A em matemática? (sim/não): ").lower()
mesada = float(input("Qual o valor da sua mesada? R$ "))
if resposta == "sim":
    total = mesada + 20
    print(f" Parabéns! Bônus de R$ 20,00! Total: R$ {total:.2f}")
else:
    print(f"Mesada normal: R$ {mesada:.2f}")
