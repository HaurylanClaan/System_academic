# disciplina.py
# -------------
# Esta classe representa uma disciplina com nome e código únicos.

class Disciplina:
    def __init__(self, nome, codigo):
        # Atributos da disciplina
        self.nome = nome      # Nome da disciplina
        self.codigo = codigo  # Código da disciplina (deve ser único e numérico)

    def __repr__(self):
        # Representação em string da disciplina (usada ao exibir na lista, por exemplo)
        return f"{self.nome} - {self.codigo}"
