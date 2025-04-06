class LancamentoNotas:
    def __init__(self):
        self.notas = {}

    def lancar_nota(self, aluno, disciplina, nota):
        if aluno not in self.notas:
            self.notas[aluno] = {}
        self.notas[aluno][disciplina] = nota

    def obter_nota(self, aluno, disciplina):
        return self.notas.get(aluno, {}).get(disciplina, None)
