# aluno.py

class Aluno:
    def __init__(self, nome, identidade, nascimento, nome_mae, nome_pai):
        self.nome = nome.strip()
        self.nome_normalizado = self.normalizar_nome(nome)
        self.identidade = identidade.strip()
        self.nascimento = nascimento.strip()
        self.nome_mae = nome_mae.strip()
        self.nome_pai = nome_pai.strip()

    def normalizar_nome(self, nome):
        """Converte o nome para minúsculas e remove espaços extras para evitar duplicatas no banco."""
        return ' '.join(nome.lower().split())
