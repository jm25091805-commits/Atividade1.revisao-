tesouro = float(input("Quantas moedas de ouro você tem? "))
if tesouro > 1000:
    desconto = tesouro * 0.10
    total = tesouro - desconto
    print(f" Imposto de 10%: -{desconto:.2f} moedas")
    print(f"Total: {total:.2f} moedas")
else:
    print(" Você não paga imposto. Tesouro intocado!")
