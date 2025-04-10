from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox, QPushButton, QTextEdit
from database import carregar_alunos_com_id, carregar_notas_por_aluno

class VerNotasWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ver Notas por Aluno")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.combo_alunos = QComboBox()
        self.alunos = carregar_alunos_com_id()
        for aluno in self.alunos:
            self.combo_alunos.addItem(aluno[1], aluno[0])  # nome, id

        layout.addWidget(QLabel("Selecione um aluno:"))
        layout.addWidget(self.combo_alunos)

        btn_ver_notas = QPushButton("Ver Notas")
        btn_ver_notas.clicked.connect(self.ver_notas)
        layout.addWidget(btn_ver_notas)

        self.resultado = QTextEdit()
        self.resultado.setReadOnly(True)
        layout.addWidget(self.resultado)

        self.setLayout(layout)

    def ver_notas(self):
        aluno_id = self.combo_alunos.currentData()
        notas = carregar_notas_por_aluno(aluno_id)

        if notas:
            texto = ""
            for disciplina, nota1, nota2, media in notas:
                texto += f"Disciplina: {disciplina}\nNota 1: {nota1}\nNota 2: {nota2}\nMédia: {media:.2f}\n\n"
            self.resultado.setText(texto)
        else:
            self.resultado.setText("Nenhuma nota encontrada para este aluno.")
