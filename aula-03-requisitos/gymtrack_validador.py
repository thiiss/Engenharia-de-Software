import time

print("="*40)
print(" GymTrack - Validador de Treino")
print("="*40)

# DADOS DO TREINO (Mude os valores para testar!)
exercicio = "Supino Reto"
peso_kg = 80
repeticoes = 10

# RF01 - Validação do nome do exercício (Não pode ser vazio) [cite: 578]
if exercicio != "":
    print(f"[RF01] Exercício válido: {exercicio}")
else:
    print(f"[RF01] ERRO: Nome do exercício não pode ser vazio.")

# RF02 - O peso deve estar entre 1 e 300 kg [cite: 585]
if 1 <= peso_kg <= 300:
    print(f"[RF02] Peso válido: {peso_kg}kg")
else:
    print(f"[RF02] ERRO: Peso fora do limite permitido (1-300kg).")

# RF03 - As repetições devem estar entre 1 e 50 [cite: 591]
if 1 <= repeticoes <= 50:
    print(f"[RF03] Repetições válidas: {repeticoes}")
else:
    print(f"[RF03] ERRO: Repetições fora do limite permitido (1-50).")

# RNF01 - O registro deve ocorrer em menos de 200ms [cite: 600]
inicio = time.time()
time.sleep(0.05) # Simula o processamento do banco de dados [cite: 604]

print("-" * 20)
print(f"Série registrada: {exercicio} | {peso_kg}kg x {repeticoes} reps")

fim = time.time()
tempo_ms = (fim - inicio) * 1000

if tempo_ms < 200:
    print(f"[RNF01] Tempo de registro: {tempo_ms:.0f}ms - Dentro do limite!")
else:
    print(f"X [RNF01] Lento demais: {tempo_ms:.0f}ms - Limite é 200ms")