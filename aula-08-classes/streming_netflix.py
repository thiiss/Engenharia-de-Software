class Filme:
    def __init__(self, titulo: str, duracao: int, genero: str):
        self.titulo = titulo
        self.duracao = duracao
        self.genero = genero

class Avaliacao:
    def __init__(self, nota: float, comentario: str):
        self.nota = nota
        self.comentario = comentario

class Usuario:
    def __init__(self, nome: str, email: str, plano: str):
        self.nome = nome
        self.email = email
        self.plano = plano
        self.avaliacoes = []

    def avaliar(self, filme, avaliacao: Avaliacao):
        data = {"filme": filme.titulo, "nota": avaliacao.nota, "coment": avaliacao.comentario}
        self.avaliacoes.append(data)
        print(f"Avaliação de {self.nome} para {filme.titulo} registrada!")

    def ver_avaliacoes(self):
        print(f"\n--- Avaliações de {self.nome} ---")
        for a in self.avaliacoes:
            print(f"Filme: {a['filme']} | Nota: {a['nota']} | Obs: {a['coment']}")

class Catalogo:
    def __init__(self, titulo: str, qtdFilmes: int = 0):
        self.titulo = titulo
        self.filmes = []

    def add_filme(self, filme: Filme):
        self.filmes.append(filme)
        
    def listar_filmes(self):
        print(f"\n--- Catálogo: {self.titulo} ---")
        for f in self.filmes:
            print(f"Título: {f.titulo} ({f.duracao} min) - Gênero: {f.genero}")

class Plataforma:
    def __init__(self, nome: str, pais: str):
        self.nome = nome
        self.pais = pais
        self.catalogo = None 

    def definir_catalogo(self, catalogo: Catalogo):
        self.catalogo = catalogo

# --- TESTE DO FLUXO ---

# 1. Instanciar Plataforma e Catálogo
netflix = Plataforma("Netflix", "EUA")
catalogo_destaque = Catalogo("Filmes em Destaque")

# 2. Criar Filmes
filme1 = Filme("Oppenheimer", 180, "Drama")
filme2 = Filme("Barbie", 114, "Comédia")

# 3. Adicionar filmes ao catálogo
catalogo_destaque.add_filme(filme1)
catalogo_destaque.add_filme(filme2)

# 4. Usuário faz avaliação
usuario = Usuario("Ana", "ana@email.com", "Premium")
av1 = Avaliacao(9.5, "Incrível! Assisti duas vezes")

usuario.avaliar(filme1, av1)

# 5. Saídas de dados
catalogo_destaque.listar_filmes()
usuario.ver_avaliacoes()