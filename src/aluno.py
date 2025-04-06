class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __repr__(self):
        return f"{self.nome} - {self.matricula}"
