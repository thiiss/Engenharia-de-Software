# =============================================================================
# EXERCÍCIO DA AULA 05: UML E DIAGRAMAS DE CASOS DE USO (GYMTRACK)
# Foco: Atores, Casos de Uso e Relacionamentos
# =============================================================================

class GymTrack:
    def __init__(self):
        # Base de dados simulada conforme a Parte 3 da aula
        self.treinos_registrados = []
        self.usuarios_logados = set()

    # UC01: Fazer Login
    def fazer_login(self, usuario):
        print(f"[Executando UC01] Realizando login para: {usuario}")
        self.usuarios_logados.add(usuario)
        return True

    # Funcionalidade do relacionamento <<extend>>
    def adicionar_observacao(self, obs):
        print(f"[EXTEND] Adicionando nota ao treino: '{obs}'")

    # UC02: Registrar Treino
    def registrar_treino(self, usuario, exercicio, peso, reps, observacao=None):
        print(f"\n--- Iniciando UC02: Registrar Treino ---")
        
        # Implementação do Relacionamento <<include>>
        # O código reflete que o UC01 (Login) é parte obrigatória do UC02
        if usuario not in self.usuarios_logados:
            print("ERRO: Requisito <<include>> não satisfeito. Usuário deve estar logado.")
            return

        # Lógica principal do Caso de Uso
        dados = {"exercicio": exercicio, "peso": peso, "reps": reps}
        self.treinos_registrados.append(dados)
        print(f"Sucesso: {exercicio} ({peso}kg) registrado por {usuario}.")

        # Implementação do Relacionamento <<extend>>
        # O código reflete que a observação é uma funcionalidade opcional e condicional
        if observacao:
            self.adicionar_observacao(observacao)

    # UC04: Visualizar Evolução (Apenas para Alunos)
    def visualizar_evolucao(self, usuario):
        if usuario in self.usuarios_logados:
            print(f"\n[UC04] Histórico de {usuario}:")
            for t in self.treinos_registrados:
                print(f"- {t['exercicio']}: {t['peso']}kg")
        else:
            print("Acesso negado.")

# =============================================================================
# TESTE DA VERSÃO OOP (Conforme exemplo da página 8 do PDF)
# =============================================================================

if __name__ == "__main__":
    app = GymTrack()

    # Cenário 1: Tentativa de uso sem cumprir o <<include>>
    app.registrar_treino("Thais", "Supino", 60, 10)

    # Cenário 2: Fluxo completo conforme o Diagrama de Casos de Uso
    app.fazer_login("Thais") # Ator Aluno inicia o sistema
    
    # Registro simples
    app.registrar_treino("Thais", "Agachamento", 80, 12)
    
    # Registro com funcionalidade <<extend>> (Observação)
    app.registrar_treino("Thais", "Leg Press", 150, 10, observacao="Focar na amplitude")

    # Visualização de resultados
    app.visualizar_evolucao("Thais")