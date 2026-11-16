nota1 = float(input("Nota da primeira prova: "))
nota2 = float(input("Nota da segunda prova: "))
media = (nota1 + nota2) / 2
print(f"Média: {media:.1f}")
if media >= 7:
    print(" Aprovado!")
elif media >= 5:
    print(" Recuperação!")
else:
    print(" Reprovado")
