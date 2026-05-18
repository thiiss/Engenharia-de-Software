class Requisito:
    def __init__(self, id, descricao, pre_condicao):
        self.id = id
        self.descricao = descricao
        self.pre_condicao = pre_condicao

def validar_srs(lista_requisitos):
    resultados = []
    
    for rf in lista_requisitos:
        erros = []
        
        # Dica 1: Descrição muito curta (falta clareza)
        if len(rf.descricao) < 20:
            erros.append("Descrição muito curta (falta clareza)")
            
        # Dica 2: Falta de pré-condição
        if rf.pre_condicao == "":
            erros.append("Pré-condição obrigatória não informada")
            
        # Dica 3: Verificar se o ID segue o padrão RF-XXX
        if not rf.id.startswith("RF-") or not any(char.isdigit() for char in rf.id):
            erros.append("ID fora do padrão de rastreabilidade (ex: RF-001)")
            
        if not erros:
            resultados.append(f"{rf.id}: VÁLIDO")
        else:
            resultados.append(f"{rf.id}: INVÁLIDO - {', '.join(erros)}")
            
    return resultados

# Testando a validação
requisitos_gym = [
    Requisito("RF-001", "O sistema deve permitir login.", "Utilizador cadastrado"), # Curto
    Requisito("002", "O sistema deve permitir o registo de pesos e repetições para cada série.", ""), # ID errado e sem pré-condição
    Requisito("RF-003", "O sistema deve gerar relatórios semanais de evolução de carga para o professor.", "Treinos registrados") # Válido
]

for status in validar_srs(requisitos_gym):
    print(status)