senha_correta = "Segredo"
senha_digitada = input("Digite a senha secreta: ")
if senha_digitada == senha_correta:
    print("Acesso liberado!")
elif senha_digitada == senha_correta.upper():
    print("Quase! Mas você gritou a senha (Caps Lock). Tente minúsculas.")
else:
    print("Senha incorreta.")
