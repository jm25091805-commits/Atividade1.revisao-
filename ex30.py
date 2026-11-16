print("=== A TAVERNA DO DRAGÃO ===")
print("Bem-vindo, aventureiro! Vamos entrar...\n")

# Passo 1: Senha Secreta
senha = input("Digite a senha secreta para entrar: ")
if senha != "Abre-te Sésamo":
    print(" Senha incorreta! A porta se fecha. Fim de jogo.")
    exit()
print(" Porta aberta! Você entrou na taverna!\n")

# Passo 2: Verificar Idade
idade = int(input("Quantos anos você tem? "))
if idade < 13:
    print(" Você é jovem! Ganhou um suco de uva!")
else:
    print(" Você é mais velho! Ganhou uma Poção Mágica!")
print()

# Passo 3: Pergunta de Personalidade
print("Escolha seu item:")
print("1 - Espada de Aço")
print("2 - Cajado Mágico")
print("3 - Escudo Protetor")
escolha = input("Digite sua escolha (1/2/3): ")
if escolha == "1":
    item = "Espada de Aço"
elif escolha == "2":
    item = "Cajado Mágico"
else:
    item = "Escudo Protetor"
print(f" Você escolheu: {item}!\n")

# Passo 4: Calcular Mesada
dinheiro = float(input("Quanto ouro você tem? R$ "))
preco_item = 35.00
print(f"O {item} custa R$ {preco_item:.2f}")
if dinheiro >= preco_item:
    troco = dinheiro - preco_item
    print(f" Compra feita! Troco: R$ {troco:.2f}")
    print(" Parabéns! Você completou todos os desafios!")
else:
    falta = preco_item - dinheiro
    print(f" Falta R$ {falta:.2f} para comprar o item. Volte depois!")
print("\n Obrigado por visitar a Taverna do Dragão!")
