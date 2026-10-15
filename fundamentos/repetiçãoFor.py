# exemplo simples de um for contador até 10
for position in range(5):
    print(f"Position: {position}")

print("Fim do loop for.")
print("Agora vamos para o próximo exemplo.")

# Laço de repetição 'for' com condição de parada
for i in range(11):
    print(f"Position: {i}")
    if i == 5:
        print("Condição de parada atingida. Saindo do loop.")
        break