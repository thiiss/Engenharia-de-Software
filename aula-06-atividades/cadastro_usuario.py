
# =============================================================================
# EXERCÍCIO DA AULA 06: DIAGRAMA DE ATIVIDADES (GYMTRACK)
# Foco: Fluxo de Processo, Decisões e Validações
# =============================================================================

import time

def registro_treino_fluxo(exercicio: str, peso: float, reps: int):
    """
    Implementação do fluxo de atividades para o processo de negócio 'Registrar Treino'.
    Baseado no diagrama de atividades da Aula 06.
    """
    
    print(f"--- [Início] Processo de Registro de Treino ---")
    
    # Atividade 1: Selecionar Exercício
    if not exercicio:
        print("[Atividade] Erro: Nenhum exercício selecionado.")
        return "Falha no Processo"
    print(f"[Atividade] Exercício selecionado: {exercicio}")

    # Nó de Decisão: Validar Peso
    # Atividade 2: Informar Carga
    while True:
        print(f"[Atividade] Informando carga: {peso}kg")
        if 1 <= peso <= 300:
            print("[Decisão] Peso Válido.")
            break
        else:
            print("[Decisão] Peso Inválido! Retornando ao início da atividade...")
            return "Falha: Peso fora dos limites"

    # Nó de Decisão: Validar Repetições
    # Atividade 3: Informar Repetições
    while True:
        print(f"[Atividade] Informando repetições: {reps}")
        if 1 <= reps <= 50:
            print("[Decisão] Repetições Válidas.")
            break
        else:
            print("[Decisão] Repetições Inválidas! Retornando ao início da atividade...")
            return "Falha: Repetições fora dos limites"

    # Atividade 4: Validar Registro (Lógica do Sistema)
    print("[Atividade] Validando consistência dos dados...")
    time.sleep(0.5)

    # Atividade 5: Salvar no Banco de Dados
    # Simulação de Fork/Join se houvesse processos paralelos (ex: Salvar + Notificar)
    try:
        print("[Atividade] Salvando registro no banco de dados...")
        time.sleep(0.3)
        print("--- [Fim] Registro concluído com Sucesso! ---")
        return "Sucesso"
    except Exception as e:
        # Caminho alternativo de erro
        print(f"[Atividade] Erro crítico ao salvar: {e}")
        print("[Atividade] Notificando erro ao usuário...")
        return "Falha no Sistema"

# =============================================================================
# TESTES DE FLUXO (Simulando as rotas do diagrama)
# =============================================================================

if __name__ == "__main__":
    print("TESTE 1: Caminho Feliz (Happy Path)")
    registro_treino_fluxo("Supino Reto", 80, 10)

    print("\nTESTE 2: Caminho de Erro (Decisão de Peso)")
    registro_treino_fluxo("Agachamento", 500, 10)

    print("\nTESTE 3: Caminho de Erro (Decisão de Repetições)")
    registro_treino_fluxo("Bíceps", 20, 99)
