# =============================================================================
# EXERCÍCIO DA AULA 07: DIAGRAMA DE SEQUÊNCIA (GYMTRACK)
# Foco: Mensagens entre objetos e Fluxo de Retorno
# =============================================================================

class BancoDeDados:
    def salvar(self, dados):
        # Simula a persistência (Mensagem de retorno: Confirmação)
        print("[DB] Dados persistidos com sucesso.")
        return True

class TreinoController:
    def __init__(self):
        self.db = BancoDeDados()

    def validar_e_registrar(self, exercicio, peso, reps):
        print(f"[Controller] Validando lógica para: {exercicio}")
        
        # Lógica de negócio (Mensagem síncrona)
        if peso > 0 and reps > 0:
            print("[Controller] Validação OK. Chamando Banco de Dados...")
            return self.db.salvar({"ex": exercicio, "p": peso, "r": reps})
        else:
            print("[Controller] X Validação Recusada: Valores inválidos.")
            return False

class AppGymTrack:
    def __init__(self):
        self.controller = TreinoController()

    def acao_registrar(self, exercicio, peso, reps):
        """
        Representa o início da linha de vida no Diagrama de Sequência.
        """
        print(f"\n[APP] Solicitando registro de {exercicio}...")
        
        # Envio de mensagem para o próximo objeto
        sucesso = self.controller.validar_e_registrar(exercicio, peso, reps)
        
        # Resposta ao Ator (Mensagem de Retorno)
        if sucesso:
            print(f"[APP] Resultado: Treino de {exercicio} salvo!")
        else:
            print(f"[APP] Resultado: Falha ao registrar treino.")

# =============================================================================
# SIMULAÇÃO DA INTERAÇÃO (TESTES)
# =============================================================================

if __name__ == "__main__":
    app = AppGymTrack()

    # Teste 1: Fluxo de Sucesso (Caminho Principal)
    app.acao_registrar("Supino Reto", 80, 10)

    # Teste 2: Fluxo de Erro (Mensagem de retorno negativa)
    app.acao_registrar("Agachamento", -10, 12)