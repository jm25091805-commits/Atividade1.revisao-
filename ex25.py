idade = int(input("Quantos anos você tem? "))
preferencia = input("Você prefere gatos ou cachorros? ").lower()
if idade < 18 and preferencia == "gatos":
    print(" Jovem e prefere gatos")
elif idade < 18 and preferencia == "cachorros":
    print(" Jovem e prefere cachorros")
elif idade >= 18 and preferencia == "gatos":
    print(" Adulto e prefere gatos")
elif idade >= 18 and preferencia == "cachorros":
    print(" Adulto e prefere cachorros")
else:
    print("Respostas não reconhecidas")
