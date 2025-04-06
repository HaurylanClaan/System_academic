class Disciplina:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo

    def __repr__(self):
        return f"{self.nome} - {self.codigo}"
